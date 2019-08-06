from django.shortcuts import render
from django.http import HttpResponse

from survey.models import SurveyUser
from survey.forms import InitialStartForm, AnswerMChoice


# Create your views here.

def index(request):
    
    # show main page

    #return HttpResponse("Survey Test")
    james = {'the_title':"Was geht!"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request,id=0):

    # save what the answers were
    if request.method == 'POST':
        form = InitialStartForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            user=form.cleaned_data['userid']

            # remember to save the data to the DB

            #CHANGE THIS TO THE DATABASE THING
            answer_list = [
                'james',
                'marc',
                'michael',
                'peter',
                'tim',
            ]

            tupelanswers = []
            i=0
            for a in answer_list:
                tupelanswers.append( (i,a) )
                i+=1
            form = AnswerMChoice()
            form.setUID(user)
            form.setAnswers(tupelanswers)


            return HttpResponse(form)
    else:
        return startSurvey()


def startSurvey(request):

    user = SurveyUser()
    
    form = InitialStartForm()
    form.setQuestions("What is your sector?", "How many employees?")
    form.setUID(user.user_id)

    allText = {
        'title':"Welcome and let's go!",
        'description':"We will start by knowing your sector and your number of employees to be able to give you a relevant recommendation in the report",
        'form':form,
    }

    return render(request, 'survey/startSurvey.html',context=allText)


def finishSurvey(request):

    # make survey readonly and show results.

    return HttpResponse("Closing stuff and give template to see report")


def showReport(request):

    # make survey readonly and show results.

    return HttpResponse("Here the report mate! in JSON of course")


def getCompanies(request):

    # get Companies contained in certain category

    return HttpResponse("Here is the JSON list of companies that are related to that category")


def continueSelfEval(request):

    return HttpResponse("If you were here, enter the code")


def loadSelfEval(request,key):

    return HttpResponse("Thank you for the key! Loading the survey and its template again")