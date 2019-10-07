from django.http import HttpResponse
from django.conf import settings

from survey.models import SurveyQuestion, SurveyQuestionAnswer, SurveyUser, SurveyUserAnswer, Recommendations
from survey.globals import SECTOR_CHOICES, COMPANY_SIZE, TRANSLATION_UI


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
            if userAnswer.uvalue > 0 and rec.answerChosen:
                finalReportRecs.append(str(rec))
            elif userAnswer.uvalue <= 0 and not rec.answerChosen:
                finalReportRecs.append(str(rec))

    return finalReportRecs


def createAndSendReport(request, userID, lang):
    from mailmerge import MailMerge
    from datetime import date
    from docx import Document
    from docx.shared import Cm, Inches, Pt

    cuser = SurveyUser.objects.filter(user_id=userID)[0]

    filepath = settings.BASE_DIR+"/wtemps/"

    theImage = filepath+"monarc.jpg"
    template = filepath+lang.lower()+"1.docx"
    doc = Document(template)
    #document = MailMerge(template)
    #doc = Document()

    score = 80
    score, detailMax, details = calculateResult(request,cuser)

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

    tfile = open(filepath+"/"+lang.lower()+"_intro.txt",'r')
    introduction = tfile.read()
    tfile.close()

    introduction = introduction.replace("\n\r","\n")
    introduction = introduction.split("\n\n")
    x = 0
    for i in introduction:
        if x == 0:
            doc.add_heading(i,level=1)
            x += 1
            continue
        doc.add_paragraph(i)


    tfile = open(filepath+"/"+lang.lower()+"_description.txt",'r')
    methodDescr = tfile.read()
    tfile.close()
    
    methodDescr = methodDescr.replace("\n\r","\n")
    methodDescr = methodDescr.split("\n\n")
    x = 0
    for i in methodDescr:
        if x == 0:
            doc.add_heading(i,level=1)
            x += 1
            continue
        doc.add_paragraph(i)
    

    tfile = open(filepath+"/"+lang.lower()+"_resultdisclaimer.txt",'r')
    results = tfile.read()
    tfile.close()

    results = results.replace("\n\r","\n")
    results = results.replace("$$result$$",str(score))
    results = results.split("\n\n")

    x = 0
    for i in results:
        if x == 0:
            doc.add_heading(i,level=1)
            x += 1
            continue
        doc.add_paragraph(i)


    doc.add_heading(TRANSLATION_UI['document']['questions'][lang.lower()],level=1)

    x = 1
    for i in everyQuestion:
        table = doc.add_table(rows=1,cols=2)
        table.autofit = False
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = str(x)
        hdr_cells[1].text = str(i)

        bX = hdr_cells[0].paragraphs[0].runs[0]
        bX.font.bold = True
        bX.font.size = Pt(13)
        bX = hdr_cells[1].paragraphs[0].runs[0]
        bX.font.bold = True
        bX.font.size = Pt(13)

        answerlist = SurveyQuestionAnswer.objects.filter(question=i).order_by('aindex')
        
        for a in answerlist:
            row_cells = table.add_row().cells
            u = SurveyUserAnswer.objects.filter(answer=a)[0]
            
            if u.uvalue > 0:
                row_cells[0].text = "X"
                bX = row_cells[0].paragraphs[0].runs[0]
                bX.font.bold = True
            else:
                row_cells[0].text = " "
            
            row_cells[1].text = str(a)
        
        col = table.columns[0]
        col.width = Cm(1.5)
        col = table.columns[1]
        col.width = Cm(14.0)
        for cell in table.columns[0].cells:
            cell.width=Cm(1.5)

        doc.add_paragraph()
        x += 1



    '''
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
            
            if u.uvalue > 0:
                line['ca'] = "X"
            else:
                line['ca'] = " "
            
            line['surveyAnswers'] = str(a)
            table.append(line)

    everyQuestionAndAnswer = table
    '''
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

    # use matplotlib for png of radar graph
    # can use matplotlib import pyplot as plt
    # then the graph save: plt.savefig('/tmp/'+str(userID)+'.png')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=result-'+lang.lower()+'.docx'
    #document.write(response)
    doc.save(response)
    # make survey readonly and show results.
    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit

    return response


def calculateResult(request, cuser):
    allQuestions = SurveyQuestion.objects.values_list('maxPoints', flat=True).order_by('qindex')
    maxscore = sum(allQuestions)
    allUserAnswers = SurveyUserAnswer.objects.filter(uvalue__gt=0,user=cuser).order_by('answer__question__qindex','answer__aindex')
    totalscore = sum([x.answer.score for x in allUserAnswers])

    maxeval = {}
    evaluation = {}
    sectionlist = {}

    for q in SurveyQuestion.objects.all():
        if q.section.id not in evaluation:
            evaluation[q.section.id] = 0
        if q.section.id not in maxeval:
            maxeval[q.section.id] = 0
        if q.section.id not in sectionlist:
            sectionlist[q.section.id] = str(q.section)
        
        maxeval[q.section.id] += q.maxPoints

        uanswers = SurveyUserAnswer.objects.filter(uvalue__gt=0,answer__question__id=q.id)
        scores = [x.answer.score for x in uanswers]
        evaluation[q.section.id] += sum(scores)

    # get the score in percent! with then 100 being maxscore
    totalscore = round((totalscore*100)/maxscore)
    
    return totalscore, maxeval, evaluation, sectionlist
