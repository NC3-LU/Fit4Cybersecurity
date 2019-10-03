from django.http import HttpResponse

from survey.models import SurveyQuestion, SurveyQuestionAnswer, SurveyUser, SurveyUserAnswer, Recommendations
from survey.globals import SECTOR_CHOICES, COMPANY_SIZE


def getRecommendations(cuser):
    allAnswers = SurveyQuestionAnswer.objects.all().order_by('question__qindex','aindex')

    #userAnswers = SurveyUserAnswer.objects.all().filter(user=cuser)

    #recommendations = Recommendations

    finalReportRecs = []

    for a in allAnswers:
        userAnswer = SurveyUserAnswer.objects.all().filter(user=cuser).filter(answer=a)[0]
        recommendation = Recommendations.objects.all().filter(forAnswer=a)

        if not recommendation.exists():
            continue

        for rec in recommendation:
            if rec.min_e_count.lower() > cuser.e_count.lower() or rec.max_e_count.lower() < cuser.e_count.lower():
                continue
            if userAnswer.value > 0 and rec.answerChosen:
                finalReportRecs.append(str(rec))
            elif userAnswer.value <= 0 and not rec.answerChosen:
                finalReportRecs.append(str(rec))

    return finalReportRecs


def createAndSendReport(request, userID, lang):
    from mailmerge import MailMerge
    from datetime import date
    from docx import Document
    from docx.shared import Cm, Inches

    cuser = SurveyUser.objects.filter(user_id=userID)[0]

    filepath = "/home/fabien/Documents/CybersecurityStarterKit/csskp/wtemps/"

    theImage = filepath+"monarc.jpg"
    template = filepath+lang.lower()+"1.docx"
    doc = Document(template)
    #document = MailMerge(template)
    #doc = Document()

    print (doc)

    theResult = 80

    everyQuestion = SurveyQuestion.objects.all().order_by('qindex')

    sectorName = str(cuser.sector)
    for a,b in SECTOR_CHOICES:
        if cuser.sector == a:
            sectorName = str(b)
    
    compSize = str(cuser.e_count)
    for a,b in COMPANY_SIZE:
        if cuser.e_count == a:
            compSize = b
    
    recommendationList = getRecommendations(cuser)
    recommendationList = "\n\n".join(recommendationList)


    table = []
    ind = 0
    for i in everyQuestion:
        ind += 1
        if ind > 1:
            table.append({'ca':"", 'surveyAnswers':""})

        answerlist = SurveyQuestionAnswer.objects.filter(question=i).order_by('aindex')
        headingLine = {'ca':str(ind), 'surveyAnswers':str(i)}
        table.append(headingLine)
        
        for a in answerlist:
            line = {'ca':"", 'surveyAnswers':""}
            u = SurveyUserAnswer.objects.filter(answer=a)[0]
            
            if u.value > 0:
                line['ca'] = "X"
            else:
                line['ca'] = " "
            
            line['surveyAnswers'] = str(a)
            table.append(line)

    everyQuestionAndAnswer = table
    
    '''
    document.merge(
        result=str(theResult)+"/100",
        companysize=compSize,
        resultGraph=theImage,
        #surveyAnswers=everyQuestionAndAnswer,
        ca=everyQuestionAndAnswer,
        sector=sectorName,
        generationDate=str(date.today()),
        recommendationsList=recommendationList,
        )
    '''

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=result'+lang.lower()+'.docx'
    #document.write(response)
    doc.save(response)
    # make survey readonly and show results.
    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit

    return response

def calculateResult(request,user):
    allQuestions = SurveyQuestion.objects.values_list('maxPoints', flat=True).order_by('qindex')
    maxscore = sum(allQuestions)
    allUserAnswers = SurveyUserAnswer.objects.filter(user=user).filter(value>0).order_by('answer__question__qindex','answer__aindex')
    totalscore = sum([x.answer.score for x in allUserAnswers])

    maxeval = {}
    evaluation = {}

    for q in SurveyQuestion.objects.all():
        if q.section.id not in evaluation:
            evaluation[q.section.id] = 0
        if q.section.id not in maxeval:
            maxeval[q.section.id] = 0
        
        maxeval[q.section.id] += q.maxPoints

        uanswers = SurveyUserAnswer.objects.filter(answer__question__id=q.id).filter(value>0)
        scores = [x.answer.score for x in uanswers]
        evaluation[q.section.id] += sum(scores)

    # get the score in percent! with then 100 being maxscore
    totalscore = round((totalscore*100)/maxscore)
    
    return totalscore, maxeval, evaluation
