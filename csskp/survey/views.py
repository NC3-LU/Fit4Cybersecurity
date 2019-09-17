from __future__ import print_function

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from survey.models import SurveyUser
from survey.forms import InitialStartForm, AnswerMChoice
from survey.viewLogic import saveAndGetQuestion, findUserById, showCompleteReport
from survey.globals import LANG_SELECT, COMPANY_SIZE



# Create your views here.

def index(request):
    
    # show main page

    # return HttpResponse("Survey Test")
    james = {'the_title':"Was geht! and choose Language"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request,id=0):

    question = saveAndGetQuestion(request,id)
    if question == -1:
        return finishSurvey(request)
    if question == None:
        return startSurvey(request)
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

    allText = {
        'title':"Welcome and let's go!",
        'description':"We will start by knowing your sector and your number of employees to be able to give you a relevant recommendation in the report",
        'form':form,
        'userId': user.user_id,
    }

    return render(request, 'survey/startSurvey.html',context=allText)


def finishSurvey(request):

    userid = request.session['user_id']

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    #return HttpResponse(showCompleteReport(request,userid))

    return showReport(request)


def showReport(request):
    userid = request.session['user_id']
    
    from mailmerge import MailMerge
    from datetime import date

    template = "/home/fabien/Documents/CybersecurityStarterKit/csskp/templateForTest.docx"
    
    document = MailMerge(template)
    print(document.get_merge_fields())

    document.merge(
        result="80/100",
        companysize=COMPANY_SIZE[5][1],
        resultGraph="SOME IMAGE HERE",
        surveyAnswers="THE COMPLETE LIST",
        sector=str(userid),
        generationDate=str(date.today()),
        recommendationsList=showCompleteReport(request,userid) 
        )

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    document.write(response)
    # make survey readonly and show results.
    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit

    return response
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
