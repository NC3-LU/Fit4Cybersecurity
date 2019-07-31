from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    
    # show main page

    #return HttpResponse("Survey Test")
    james = {'the_title':"Was geht!"}

    return render(request,'survey/index.html',context=james)


def gotoQuestion(request):

    # save what the answers were

    return HttpResponse("some JSON here")


def finishSurvey(request):

    # make survey readonly and show results.

    return HttpResponse("Here the report mate! in JSON of course")


def getCompanies(request):

    # get Companies contained in certain category

    return HttpResponse("Here is the JSON list of companies that are related to that category")