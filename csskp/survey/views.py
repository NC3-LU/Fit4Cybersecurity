from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    
    # show main page

    #return HttpResponse("Survey Test")
    james = {'the_title':"Was geht!"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request,id=0):

    # save what the answers were

    return HttpResponse("some JSON here")


def startSurvey(request):

    return HttpResponse("Some template here and then start the rest")


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