from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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

    form_data = handleStartSurvey(user, request)

    return render(request, 'survey/questions.html', context=form_data)


def getQuestion(request):

    if request.session.get('user_id', None) is None:
        return HttpResponseRedirect('/')

    user = findUserById(request.session['user_id'])
    question = saveAndGetQuestion(user, request)

    if question == -1:
        return finish(request)

    return render(request, 'survey/questions.html', context=question)


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
        'description': TRANSLATION_UI['report']['description'][user_lang],
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

    return render(request, 'survey/finishedSurvey.html', context=textLayout)


def showReport(request, lang):
    return createAndSendReport(findUserById(request.session['user_id']), lang)


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
