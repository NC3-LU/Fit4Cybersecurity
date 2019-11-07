from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _
from django import forms

from survey.viewLogic import handle_start_survey, handle_question_answers_request, find_user_by_id, get_questions_with_user_answers
from survey.reporthelper import calculateResult, createAndSendReport, getRecommendations
from survey.globals import TRANSLATION_UI, MIN_ACCEPTABLE_SCORE
from survey.models import SURVEY_STATUS_IN_PROGRESS, SURVEY_STATUS_PREVIEW, SURVEY_STATUS_FINISHED, SurveyUser
from django.contrib import messages
from uuid import UUID
from csskp.settings import HASH_KEY
from cryptography.fernet import Fernet


def index(request):
    return render(request, 'survey/index.html')


def start(request, lang="EN"):
    try:
        form_data = handle_start_survey(request, lang)
        if isinstance(form_data, SurveyUser):
            return HttpResponseRedirect('/survey/question/' + str(form_data.current_qindex))
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

    add_form_translations(form_data, lang, 'question')

    return render(request, 'survey/start.html', context=form_data)


def handle_question_form(request, question_index: int):
    if request.session.get('user_id', None) is None:
        return HttpResponseRedirect('/')

    user = find_user_by_id(request.session['user_id'])
    if user.status == SURVEY_STATUS_FINISHED:
        return HttpResponseRedirect('/survey/finish')
    elif user.current_qindex < question_index or question_index <= 0:
        return HttpResponseRedirect('/survey/question/' + str(user.current_qindex))

    preview_ancher = ''
    if user.status == SURVEY_STATUS_PREVIEW:
        preview_ancher = '#question-' + str(question_index)

    form_data = handle_question_answers_request(request, user, question_index)

    if form_data is None:
        if user.status == SURVEY_STATUS_PREVIEW:
            return HttpResponseRedirect('/survey/preview' + preview_ancher)
        else:
            return HttpResponseRedirect('/survey/question/' + str(user.current_qindex))

    add_form_translations(form_data, user.chosenLang, 'question')

    return render(request, 'survey/questions.html', context=form_data)


def show_report(request, lang):
    user_id = request.session['user_id']
    user = find_user_by_id(user_id)
    if user.status != SURVEY_STATUS_FINISHED:
        messages.error(request, _('To generate a report you have to finish the survey.'))

        return HttpResponseRedirect('/')

    try:
        return createAndSendReport(user, lang)
    except Exception as e:
        messages.warning(request, e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def preview(request):
    user_id = request.session['user_id']
    user = find_user_by_id(user_id)
    if user.status == SURVEY_STATUS_FINISHED:
        return HttpResponseRedirect('/survey/finish')
    elif user.is_survey_in_progress():
        return HttpResponseRedirect('/survey/question/' + str(user.current_qindex))

    if request.method == 'POST' and forms.Form(data=request.POST).is_valid():
        user.status = SURVEY_STATUS_FINISHED
        user.save()

        return HttpResponseRedirect('/survey/finish')

    questions_with_user_answers = get_questions_with_user_answers(user)

    lang = user.chosenLang.lower()

    textLayout = {
        'questions_with_user_answers': questions_with_user_answers,
        'form': forms.Form(),
        'user': user,
        'translations': {
            'title': TRANSLATION_UI['preview']['title'][lang],
            'validate_answers_button': TRANSLATION_UI['preview']['validate_answers_button'][lang],
            'modify_button': TRANSLATION_UI['preview']['modify_button'][lang],
            'continue_later': {
                'button': TRANSLATION_UI['question']['continue_later']['button'][lang],
                'title': TRANSLATION_UI['question']['continue_later']['title'][lang],
                'text': TRANSLATION_UI['question']['continue_later']['text'][lang],
                'button_download': TRANSLATION_UI['question']['continue_later']['button_download'][lang],
                'button_close': TRANSLATION_UI['question']['continue_later']['button_close'][lang],
            },
        },
    }

    return render(request, 'survey/preview.html', context=textLayout)


def finish(request):
    user_id = request.session['user_id']
    user = find_user_by_id(user_id)
    if user.status != SURVEY_STATUS_FINISHED:
        return HttpResponseRedirect('/')

    user_lang = user.chosenLang.lower()

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    txt_score, radar_current, sections_list = calculateResult(user, user_lang.upper())

    diagnostic_email_body = TRANSLATION_UI['report']['request_diagnostic']['email_body'][user_lang]

    recommendations = getRecommendations(user, user_lang.upper())
    # To properly display breaking lines \n on html page.
    for rx in recommendations:
        recommendations[rx] = [x.replace("\n", "<br>") for x in recommendations[rx]]

    textLayout = {
        'title': "Fit4Cybersecurity - " + TRANSLATION_UI['report']['title'][user_lang],
        'description': TRANSLATION_UI['report']['description'][user_lang],
        'recommendations': recommendations,
        'user': user,
        'reportlink': "/survey/report",
        'txtscore': txt_score,
        'chartTitles': str(sections_list),
        'chartlabelYou': TRANSLATION_UI['report']['result'][user_lang],
        'chartdataYou': str(radar_current),
        'min_acceptable_score': MIN_ACCEPTABLE_SCORE,
    }

    add_form_translations(textLayout, user.chosenLang, 'report')

    crypter = Fernet(HASH_KEY)

    textLayout['translations']['request_diagnostic'] = {
        'title': TRANSLATION_UI['report']['request_diagnostic']['title'][user_lang],
        'description': TRANSLATION_UI['report']['request_diagnostic']['description'][user_lang],
        'service_fee': TRANSLATION_UI['report']['request_diagnostic']['service_fee'][user_lang],
        'email_subject': TRANSLATION_UI['report']['request_diagnostic']['email_subject'][user_lang],
        'email_body': diagnostic_email_body.replace('{userId}', str(crypter.encrypt(user_id.encode('utf-8'))))
    }
    textLayout['translations']['txtdownload'] = TRANSLATION_UI['report']['download'][user_lang]
    textLayout['translations']['txtreport'] = TRANSLATION_UI['report']['report'][user_lang]

    return render(request, 'survey/finishedSurvey.html', context=textLayout)


def get_companies(request):
    """Get Companies contained in certain category.
    Returns a company list related to the selected recommendations"""
    return HttpResponse("Here is the JSON list of companies that are related to that category")


def resume(request):
    try:
        user_id = UUID(request.GET.get('user_id'))

        user = find_user_by_id(str(user_id))
    except:
        messages.warning(request, _('We could not find a survey with the requested key, please start a new one.'))
        return HttpResponseRedirect('/')

    request.session['user_id'] = str(user_id)

    if user.is_survey_in_progress():
        return HttpResponseRedirect('/survey/question/' + str(user.current_qindex))

    if user.status == SURVEY_STATUS_PREVIEW:
        return HttpResponseRedirect('/survey/preview')

    if user.status == SURVEY_STATUS_FINISHED:
        return HttpResponseRedirect('/survey/finish')

    return HttpResponseRedirect('/')


def add_form_translations(data, lang: str, topic='question'):
    data['translations'] = {
        'continue_later': {
            'button': TRANSLATION_UI[topic]['continue_later']['button'][lang.lower()],
            'title': TRANSLATION_UI[topic]['continue_later']['title'][lang.lower()],
            'text': TRANSLATION_UI[topic]['continue_later']['text'][lang.lower()],
            'button_download': TRANSLATION_UI[topic]['continue_later']['button_download'][lang.lower()],
            'button_close': TRANSLATION_UI[topic]['continue_later']['button_close'][lang.lower()],
        },
        'leave_survey': {
            'title': TRANSLATION_UI[topic]['leave_survey']['title'][lang.lower()],
            'yes': TRANSLATION_UI[topic]['leave_survey']['yes'][lang.lower()],
            'no': TRANSLATION_UI[topic]['leave_survey']['no'][lang.lower()],
        }
    }

    if 'next_button' in TRANSLATION_UI[topic]:
        data['translations']['next_button'] = TRANSLATION_UI[topic]['next_button'][lang.lower()]
    if 'back_button' in TRANSLATION_UI[topic]:
        data['translations']['back_button'] = TRANSLATION_UI[topic]['back_button'][lang.lower()]
    if 'modify_button' in TRANSLATION_UI[topic]:
        data['translations']['modify_button'] = TRANSLATION_UI[topic]['modify_button'][lang.lower()]
    if 'cancel_button' in TRANSLATION_UI[topic]:
        data['translations']['cancel_button'] = TRANSLATION_UI[topic]['cancel_button'][lang.lower()]
    if 'select_multi_descr' in TRANSLATION_UI[topic]:
        data['translations']['select_multi_descr'] = TRANSLATION_UI[topic]['select_multi_descr'][lang.lower()]


def get_terms(request):
    return render(request, 'survey/terms.html')
