import os
from django.http import HttpResponse
from django.conf import settings

from csskp.settings import PICTURE_DIR
from survey.models import SurveyQuestion, SurveyQuestionAnswer, SurveyUser, SurveyUserAnswer, Recommendations, \
    TranslationKey
from survey.globals import TRANSLATION_UI
from utils.radarFactory import radar_factory
import matplotlib.pyplot as plt



def getRecommendations(user: SurveyUser, lang: str):
    allAnswers = SurveyQuestionAnswer.objects.all().order_by('question__qindex', 'aindex')
    translations = TranslationKey.objects.filter(lang=lang, ttype='R')
    translation_key_values = {}
    for translation in translations:
        translation_key_values[translation.key] = translation.text

    finalReportRecs = {}

    for a in allAnswers:
        userAnswer = SurveyUserAnswer.objects.filter(user=user).filter(answer=a)[0]
        recommendations = Recommendations.objects.filter(forAnswer=a)

        if not recommendations.exists():
            continue

        if a.question.id not in finalReportRecs:
            finalReportRecs[a.question.id] = []

        for rec in recommendations:
            if rec.min_e_count.lower() > user.e_count.lower() or rec.max_e_count.lower() < user.e_count.lower():
                continue
            if (userAnswer.uvalue > 0 and rec.answerChosen) or (userAnswer.uvalue <= 0 and not rec.answerChosen):
                finalReportRecs[a.question.id].append(translation_key_values[rec.textKey])

        if len(finalReportRecs[a.question.id])<=0:
            del finalReportRecs[a.question.id]

    return finalReportRecs


def createAndSendReport(user: SurveyUser, lang):
    """Generates the report as a .dox file, then returns it to the view.
    """
    from docx import Document
    from docx.shared import Cm, Pt
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from datetime import date

    filepath = settings.BASE_DIR+"/wtemps/"

    template = filepath + "template.docx"
    doc = Document(template)

    everyQuestion = SurveyQuestion.objects.all().order_by('qindex')

    introduction = ""
    file_path = os.path.join(filepath, lang.lower() + '_intro.txt')
    try:
        with open(file_path, 'r') as f:
            introduction = f.read()
    except Exception as e:
        #raise e
        raise Exception('Missing file: {}'.format(file_path))

    introduction = introduction.replace("\n\r", "\n")
    introduction = introduction.split("\n\n")
    x = 0
    for i in introduction:
        if x == 0:
            doc.add_heading(i, level=1)
            x += 1
            continue
        doc.add_paragraph(i)

    methodDescr = ""
    file_path = os.path.join(filepath, lang.lower() + '_description.txt')
    try:
        with open(file_path, 'r') as f:
            methodDescr = f.read()
    except:
        raise Exception('Missing file: {}'.format(file_path))

    methodDescr = methodDescr.replace("\n\r", "\n")
    methodDescr = methodDescr.replace("$$qnumber$$", str(len(SurveyQuestion.objects.all())))
    methodDescr = methodDescr.split("\n\n")
    x = 0
    for i in methodDescr:
        if x == 0:
            doc.add_heading(i, level=1)
            x += 1
            continue
        doc.add_paragraph(i)

    results = ""
    file_path = os.path.join(filepath, lang.lower() + '_resultdisclaimer.txt')
    try:
        with open(file_path, 'r') as f:
            results = f.read()
    except:
        raise Exception('Missing file: {}'.format(file_path))

    score, detail_max, details, section_list = calculateResult(user)

    results = results.replace("\n\r", "\n")
    #results = results.replace("$$result$$", str(score))
    results = results.split("\n\n")

    x = 0
    for i in results:
        if x == 0:
            doc.add_heading(i, level=1)
            x += 1

            continue
        if "$$result$$" in i:
            i = i.split("$$result$$")
            p = doc.add_paragraph()
            ind = 1
            for x in i:
                p.add_run(x)
                #p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                if ind < len (i):
                    px = p.add_run(str(score))
                    px.font.bold = True
                ind += 1
        else:
            doc.add_paragraph(i)

    try:
        chart_png_file = generate_chart_png(user, detail_max, details, section_list, lang)
        doc.add_paragraph()
        paragraph = doc.add_paragraph()
        run = paragraph.add_run()
        run.add_picture(chart_png_file)
    except:
        pass

    doc.add_paragraph()
    recommendationList = getRecommendations(user, lang)
    #recommendationList = "\n\n".join(recommendationList)

    doc.add_page_break()

    recs = ""
    file_path = os.path.join(filepath, lang.lower() + '_recs.txt')
    try:
        with open(file_path, 'r') as f:
            recs = f.read()
    except Exception as e:
        #raise e
        raise Exception('Missing file: {}'.format(file_path))

    recs = recs.replace("\n\r", "\n")
    recs = recs.split("\n\n")
    x = 0
    for i in recs:
        if x == 0:
            doc.add_heading(i, level=1)
            x += 1
            continue
        doc.add_paragraph(i)


    x=1
    for recLst in recommendationList:
        doc.add_paragraph(str(x)+". ")
        rec = recommendationList[recLst]
        rec = "\n".join(rec)
        doc.add_paragraph(rec, "List Paragraph")
        x+=1

    doc.add_page_break()

    doc.add_heading(TRANSLATION_UI['document']['questions'][lang.lower()], level=1)

    for index, question in enumerate(everyQuestion):
        table = doc.add_table(rows=1, cols=2)
        table.autofit = False
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = str(index+1)
        hdr_cells[1].text = str(question)

        bX = hdr_cells[0].paragraphs[0].runs[0]
        bX.font.bold = True
        bX.font.size = Pt(13)
        bX = hdr_cells[1].paragraphs[0].runs[0]
        bX.font.bold = True
        bX.font.size = Pt(13)

        answerlist = SurveyQuestionAnswer.objects.filter(question=question).order_by('aindex')

        for a in answerlist:
            row_cells = table.add_row().cells
            u = SurveyUserAnswer.objects.filter(answer=a)[0]

            if u.uvalue > 0:
                row_cells[0].text = "X"
                bX = row_cells[0].paragraphs[0].runs[0]
                bX.font.bold = True
            else:
                row_cells[0].text = " "

            if u.uvalue > 0:
                bX = row_cells[1].paragraphs[0].runs[0]
                bX.font.bold = True
                
            row_cells[1].text = str(a)

        col = table.columns[0]
        col.width = Cm(1.0)
        col = table.columns[1]
        col.width = Cm(14.0)
        for cell in table.columns[0].cells:
            cell.width = Cm(1.0)
        for cell in table.columns[1].cells:
            cell.width = Cm(14.0)

        doc.add_paragraph()

    '''
    sectorName = str(user.sector)
    # SECTOR_CHOICES is removed!
    for a,b in SECTOR_CHOICES:
        if user.sector == a:
            sectorName = str(b)

    compSize = str(user.e_count)
    for a,b in COMPANY_SIZE:
        if user.e_count == a:
            compSize = b

    recommendationList = getRecommendations(user, lang)
    recommendationList = "\n\n".join(recommendationList)

    table = []
    ind = 0
    for question in everyQuestion:
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

    section = doc.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.text = str(date.today())+"\t\tFit4Cybersecurity"
    paragraph.style = doc.styles["Header"]


    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=result-'+lang.lower()+'.docx'
    doc.save(response)

    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit

    return response


def calculateResult(user: SurveyUser):
    allUserAnswers = SurveyUserAnswer.objects.filter(uvalue__gt=0, user=user).order_by('answer__question__qindex',
                                                                                       'answer__aindex')
    totalscore = sum([x.answer.score for x in allUserAnswers])

    maxeval = {}
    evaluation = {}
    sectionlist = {}
    maxscore = 0

    translations = TranslationKey.objects.filter(lang=user.chosenLang, ttype='S')
    translation_key_values = {}
    for translation in translations:
        translation_key_values[translation.key] = translation.text

    for q in SurveyQuestion.objects.all():
        maxscore += q.maxPoints
        if q.section.id not in evaluation:
            evaluation[q.section.id] = 0
        if q.section.id not in maxeval:
            maxeval[q.section.id] = 0
        sectionlist[q.section.id] = translation_key_values[q.section.sectionTitleKey]

        maxeval[q.section.id] += q.maxPoints

        uanswers = SurveyUserAnswer.objects.filter(user=user, uvalue__gt=0, answer__question__id=q.id)
        scores = [x.answer.score for x in uanswers]
        evaluation[q.section.id] += sum(scores)

    # get the score in percent! with then 100 being maxscore
    totalscore = round((totalscore * 100) / maxscore)

    sectionlist = [sectionlist[x] for x in sectionlist]
    evaluation = [evaluation[x] for x in evaluation]
    maxeval = [maxeval[x] for x in maxeval]

    return totalscore, maxeval, evaluation, sectionlist


def generate_chart_png(user: SurveyUser, max_eval, evaluation, sections_list, lang):
    """Generates the chart with Matplotlib and returns the path of the generated
    graph which will be included in the report.
    """
    n = len(sections_list)
    theta = radar_factory(n, frame='polygon')

    spoke_labels = []
    for section in sections_list:
        spoke_labels.append(section)

    fig, ax = plt.subplots(figsize=(7, 5), dpi=150, nrows=1, ncols=1,
                             subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    grid_step = max(max_eval) / 5
    ax.set_rgrids([0, grid_step, grid_step * 2, grid_step * 3, grid_step * 4])
    ax.set_ylim(0, max(max_eval))

    ax.plot(theta, evaluation, color='r')
    ax.fill(theta, evaluation, facecolor='r', alpha=0.25)

    ax.plot(theta, max_eval, color='b')
    ax.fill(theta, max_eval, facecolor='b', alpha=0.25)

    ax.set_varlabels(spoke_labels)

    ax.legend([TRANSLATION_UI['report']['result'][lang.lower()],
               TRANSLATION_UI['report']['resultMax'][lang.lower()]], loc=(0.9, .95),
              labelspacing=0.1, fontsize='small')

    fig.text(1.0, 1.0, TRANSLATION_UI['report']['chart'][lang.lower()],
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    if not os.path.isdir(PICTURE_DIR):
        os.makedirs(PICTURE_DIR)
    file_name = os.path.join(PICTURE_DIR, 'survey-{}.png'.format(user.user_id))
    try:
        res = plt.savefig(file_name)
    except Exception as e:
        print('Error: Problem when generating picture for the report.')
        return ''
    finally:
        plt.close()

    return file_name
