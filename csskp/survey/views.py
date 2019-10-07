from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from survey.viewLogic import createUser, handleStartSurvey, saveAndGetQuestion, findUserById, showCompleteReport, createAndSendReport
from survey.globals import TRANSLATION_UI
from django.contrib import messages



def index(request):

    # show main page

    james = {'the_title': "Fit4Cybersecurity - Welcome!"}
    print('Generationg shart...')
    show_chart()
    return render(request, 'survey/index.html', context=james)

### Example:

from matplotlib import pylab

def show_chart():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    p2 = plt.bar(ind, womenMeans, width,
                 bottom=menMeans, yerr=womenStd)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    plt.show()


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

    userid = request.session['user_id']
    userlang = request.session['lang'].lower()

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    txtdownload = TRANSLATION_UI['report']['download'][userlang]
    txtreport = TRANSLATION_UI['report']['report'][userlang]
    txtdescription = TRANSLATION_UI['report']['description'][userlang]
    txttitle = TRANSLATION_UI['report']['title'][userlang]

    textLayout = {
        'title': "Fit4Cybersecurity - " + txttitle,
        'description': txtdescription,
        'recommendations': showCompleteReport(request, userid),
        'userId': userid,
        'reportlink': "/survey/report",
        'txtdownload': txtdownload,
        'txtreport': txtreport,
    }

    return render(request, 'survey/finishedSurvey.html', context=textLayout)


def showReport(request, lang):
    userid = request.session['user_id']

    return createAndSendReport(request, userid, lang)


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
