from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _

from survey.viewLogic import createUser, handleStartSurvey, saveAndGetQuestion, findUserById, getRecommendationsReport
from survey.reporthelper import calculateResult, createAndSendReport
from survey.globals import TRANSLATION_UI
from django.contrib import messages


def index(request):
    james = {'the_title': "Fit4Cybersecurity - Welcome!"}

    return render(request, 'survey/index.html', context=james)


def start(request, lang="EN"):

    if request.method == 'GET':
        user = createUser(lang)

        request.session['lang'] = user.chosenLang
        request.session['user_id'] = str(user.user_id)
    else:
        if request.session.get('user_id', None) is None:
            return HttpResponseRedirect('/')

        user = findUserById(request.session['user_id'])

    try:
        form_data = handleStartSurvey(user, request)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

    add_form_translations(form_data, user, 'question')

    return render(request, 'survey/questions.html', context=form_data)


def getQuestion(request):

    if request.session.get('user_id', None) is None:
        return HttpResponseRedirect('/')

    user = findUserById(request.session['user_id'])
    form_data = saveAndGetQuestion(user, request)

    if form_data == -1:
        return finish(request)

    add_form_translations(form_data, user, 'question')

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

    txt_score, radar_max, radar_current, sections_list = calculateResult(user)

    textLayout = {
        'title': "Fit4Cybersecurity - " + TRANSLATION_UI['report']['title'][user_lang],
        'description': _('This is the list of recommendations to improve the information security maturity in your company, provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey.'),
        'recommendations': getRecommendationsReport(user),
        'userId': user_id,
        'reportlink': "/survey/report",
        'txtdownload': TRANSLATION_UI['report']['download'][user_lang],
        'txtreport': TRANSLATION_UI['report']['report'][user_lang],
        'txtscore': txt_score,
        'chartTitles': str(sections_list),
        'chartlabelYou': TRANSLATION_UI['report']['result'][user_lang],
        'chartlabelMax': TRANSLATION_UI['report']['resultMax'][user_lang],
        'chartdataYou': str(radar_current),
        'chartdataMax': str(radar_max),
        'chartMax': max(radar_max),
    }

    add_form_translations(textLayout, user, 'report')

    return render(request, 'survey/finishedSurvey.html', context=textLayout)


def getCompanies(request):

    # get Companies contained in certain category
    # just a company list related to the selected recommendations
    return HttpResponse("Here is the JSON list of companies that are related to that category")


def resume(request, userId):
    try:
        findUserById(str(userId))
    except:
        messages.warning(request, 'We could not find a survey with te requested key, please start a new one.')
        return HttpResponseRedirect('/')

    request.session['user_id'] = str(userId)

    return HttpResponseRedirect('/survey/question')


def add_form_translations(data, user, topic='question'):
    next_button_text = ''
    if 'next_button' in TRANSLATION_UI[topic]:
        next_button_text = TRANSLATION_UI[topic]['next_button'][user.chosenLang.lower()]

    data['translations'] = {
        'continue_later': {
            'button': TRANSLATION_UI[topic]['continue_later']['button'][user.chosenLang.lower()],
            'title': TRANSLATION_UI[topic]['continue_later']['title'][user.chosenLang.lower()],
            'text': TRANSLATION_UI[topic]['continue_later']['text'][user.chosenLang.lower()],
            'button_download': TRANSLATION_UI[topic]['continue_later']['button_download'][user.chosenLang.lower()],
            'button_close': TRANSLATION_UI[topic]['continue_later']['button_close'][user.chosenLang.lower()],
        },
        'next_button': next_button_text,
    }
