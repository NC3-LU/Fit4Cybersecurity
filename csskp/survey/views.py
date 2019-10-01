from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from survey.models import SurveyUser
from survey.forms import InitialStartForm, AnswerMChoice
from survey.viewLogic import saveAndGetQuestion, findUserById, showCompleteReport, createAndSendReport
from survey.globals import LANG_SELECT,TRANSLATION_UI



# Create your views here.

def index(request):
    
    # show main page

    # return HttpResponse("Survey Test")
    james = {'the_title':"Fit4Cybersecurity - Welcome!"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request,id=0):
    userlang = request.session['lang'].lower()
    question = saveAndGetQuestion(request,id)
    if question == -1:
        return finishSurvey(request)
    if question == None:
        return startSurvey(request)
    question['txtcontinuelater'] = TRANSLATION_UI['question']['continuelater'][userlang]
    return render(request, 'survey/questions.html',context=question)
    

def startSurvey(request,lang="EN"):
    user = SurveyUser()
    
    # prevent the use of custom languages
    langs = [ x[0] for x in LANG_SELECT ]
    if lang in langs:
        user.chosenLang = lang
    else:
        user.chosenLang = LANG_SELECT[0][0]
    user.save()
    
    request.session['lang'] = user.chosenLang
    request.session['user_id'] = str(user.user_id)

    form = InitialStartForm()
    form.setUID(user.user_id)

    txtdescription = TRANSLATION_UI['question']['description'][user.chosenLang.lower()]
    txtcontinuelater = TRANSLATION_UI['question']['continuelater'][user.chosenLang.lower()]
    txttitle = TRANSLATION_UI['question']['title'][user.chosenLang.lower()]

    allText = {
        'title':"Fit4Cybersecurity - "+txttitle,
        'description':txtdescription,
        'form':form,
        'userId': user.user_id,
        'txtcontinuelater':txtcontinuelater,
    }

    return render(request, 'survey/startSurvey.html',context=allText)


def finishSurvey(request):

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
        'title': "Fit4Cybersecurity - "+txttitle,
        'description': txtdescription,
        'recommendations': showCompleteReport(request,userid),
        'userId': userid,
        'reportlink': "/survey/report",
        'txtdownload': txtdownload,
        'txtreport': txtreport,
    }

    return render(request, 'survey/finishedSurvey.html',context=textLayout)

    #return showReport(request)


def showReport(request, lang):
    userid = request.session['user_id']
    userlang = request.session['lang']

    return createAndSendReport(request, userid, lang)
    #return finishSurvey(request)


def getCompanies(request):

    # get Companies contained in certain category
    # just a company list related to the selected recommendations
    return HttpResponse("Here is the JSON list of companies that are related to that category")


def loadSelfEval(request, userId):
    try:
        user = findUserById(str(userId))
    except:
        return HttpResponseNotFound('User not found')

    request.session['lang'] = user.chosenLang
    request.session['user_id'] = str(userId)

    return HttpResponseRedirect('/survey/gotoquestion/' + str(user.current_question))
