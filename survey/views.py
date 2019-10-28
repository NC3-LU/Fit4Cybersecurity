from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _

from survey.viewLogic import createUser, handleStartSurvey, saveAndGetQuestion, findUserById
from survey.reporthelper import calculateResult, createAndSendReport, getRecommendations
from survey.globals import TRANSLATION_UI, MIN_ACCEPTABLE_SCORE
from django.contrib import messages


def index(request):
    return render(request, 'survey/index.html')


def start(request, lang="EN"):
    try:
        form_data = handleStartSurvey(request, lang)
        if form_data is None:
            return HttpResponseRedirect('/survey/question')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

    add_form_translations(form_data, lang, 'question')

    return render(request, 'survey/questions.html', context=form_data)


def getQuestion(request):

    if request.session.get('user_id', None) is None:
        return HttpResponseRedirect('/')

    user = findUserById(request.session['user_id'])
    form_data = saveAndGetQuestion(user, request)

    if form_data == -1:
        return finish(request)

    add_form_translations(form_data, user.chosenLang, 'question')

    return render(request, 'survey/questions.html', context=form_data)


def showReport(request, lang):
    try:
        return createAndSendReport(findUserById(request.session['user_id']), lang)
    except Exception as e:
        messages.warning(request, e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def finish(request):

    user_id = request.session['user_id']
    user = findUserById(user_id)
    user_lang = user.chosenLang.lower()

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    txt_score, radar_current, sections_list = calculateResult(user, user_lang.upper())

    diagnostic_email_body = TRANSLATION_UI['report']['request_diagnostic']['email_body'][user_lang]

    textLayout = {
        'title': "Fit4Cybersecurity - " + TRANSLATION_UI['report']['title'][user_lang],
        'description': TRANSLATION_UI['report']['description'][user_lang],
        'recommendations': getRecommendations(user, user_lang.upper()),
        'userId': user_id,
        'reportlink': "/survey/report",
        'txtscore': txt_score,
        'chartTitles': str(sections_list),
        'chartlabelYou': TRANSLATION_UI['report']['result'][user_lang],
        'chartdataYou': str(radar_current),
        'min_acceptable_score': MIN_ACCEPTABLE_SCORE,
    }

    add_form_translations(textLayout, user.chosenLang, 'report')

    textLayout['translations']['request_diagnostic'] = {
        'title': TRANSLATION_UI['report']['request_diagnostic']['title'][user_lang],
        'description': TRANSLATION_UI['report']['request_diagnostic']['description'][user_lang],
        'service_fee': TRANSLATION_UI['report']['request_diagnostic']['service_fee'][user_lang],
        'email_subject': TRANSLATION_UI['report']['request_diagnostic']['email_subject'][user_lang],
        'email_body': diagnostic_email_body.replace('{userId}', user_id)
    }
    textLayout['translations']['txtdownload'] = TRANSLATION_UI['report']['download'][user_lang]
    textLayout['translations']['txtreport'] = TRANSLATION_UI['report']['report'][user_lang]

    return render(request, 'survey/finishedSurvey.html', context=textLayout)


def getCompanies(request):
    """Get Companies contained in certain category.
    Returns a company list related to the selected recommendations"""
    return HttpResponse("Here is the JSON list of companies that are related to that category")


def resume(request, userId):
    try:
        findUserById(str(userId))
    except:
        messages.warning(request, _('We could not find a survey with the requested key, please start a new one.'))
        return HttpResponseRedirect('/')

    request.session['user_id'] = str(userId)

    return HttpResponseRedirect('/survey/question')


def add_form_translations(data, lang: str, topic='question'):
    next_button_text = ''
    if 'next_button' in TRANSLATION_UI[topic]:
        next_button_text = TRANSLATION_UI[topic]['next_button'][lang.lower()]

    data['translations'] = {
        'continue_later': {
            'button': TRANSLATION_UI[topic]['continue_later']['button'][lang.lower()],
            'title': TRANSLATION_UI[topic]['continue_later']['title'][lang.lower()],
            'text': TRANSLATION_UI[topic]['continue_later']['text'][lang.lower()],
            'button_download': TRANSLATION_UI[topic]['continue_later']['button_download'][lang.lower()],
            'button_close': TRANSLATION_UI[topic]['continue_later']['button_close'][lang.lower()],
        },
        'next_button': next_button_text,
        'leave_survey': {
            'title': TRANSLATION_UI[topic]['leave_survey']['title'][lang.lower()],
            'yes': TRANSLATION_UI[topic]['leave_survey']['yes'][lang.lower()],
            'no': TRANSLATION_UI[topic]['leave_survey']['no'][lang.lower()],
        }
    }


def getTerms(request):
    return render(request, 'survey/terms.html')
