from django.shortcuts import render
from django.http import HttpResponse

from survey.models import SurveyUser
from survey.forms import InitialStartForm, AnswerMChoice
from survey.viewLogic import saveAndGetQuestion


# Create your views here.

def index(request):
    
    # show main page

    # return HttpResponse("Survey Test")
    james = {'the_title':"Was geht!"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request,id=0):

    question = saveAndGetQuestion(request,id)
    if question == -1:
        return finishSurvey(request)
    if question == None:
        return startSurvey(request)
    return render(request, 'survey/questions.html',context=question)
    


def startSurvey(request):

    user = SurveyUser()
    user.save()
    
    form = InitialStartForm()
    form.setUID(user.user_id)

    allText = {
        'title':"Welcome and let's go!",
        'description':"We will start by knowing your sector and your number of employees to be able to give you a relevant recommendation in the report",
        'form':form,
    }

    return render(request, 'survey/startSurvey.html',context=allText)


def finishSurvey(request):

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    return HttpResponse("Closing stuff and give template to see report")


def showReport(request):

    # make survey readonly and show results.
    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit
    return HttpResponse("Here the report mate! in JSON of course")


def getCompanies(request):

    # get Companies contained in certain category
    # just a company list related to the selected recommendations
    return HttpResponse("Here is the JSON list of companies that are related to that category")


def continueSelfEval(request):

    # show page to enter secret key - uuid from user
    return HttpResponse("If you were here, enter the code")


def loadSelfEval(request,key):

    # you have uuid, so get the user current question and load the next question after that.
    return HttpResponse("Thank you for the key! Loading the survey and its template again")