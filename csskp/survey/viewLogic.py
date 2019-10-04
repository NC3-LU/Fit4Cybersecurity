from django.http import HttpResponse
from django.utils.html import format_html, mark_safe

from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer, SurveyUserAnswer, TranslationKey, Recommendations
from survey.forms import InitialStartForm, AnswerMChoice
from survey.globals import LANG_SELECT, COMPANY_SIZE, SECTOR_CHOICES, TRANSLATION_UI


def createUser(lang):

    user = SurveyUser()

    # prevent the use of custom languages
    langs = [x[0] for x in LANG_SELECT]
    if lang in langs:
        user.chosenLang = lang
    else:
        user.chosenLang = LANG_SELECT[0][0]

    user.save()

    return user


def handleStartSurvey(user: SurveyUser, request):

    action = '/survey/start/' + user.chosenLang
    question = TRANSLATION_UI['question']['description'][user.chosenLang.lower()]
    title = "Fit4Cybersecurity - " + TRANSLATION_UI['question']['title'][user.chosenLang.lower()]

    if request.method == 'POST':

        form = InitialStartForm(data=request.POST)

        if form.is_valid():
            user.sector = form.cleaned_data['sector']
            user.e_count = form.cleaned_data['compSize']
            user.current_question = 1
            user.save()

            survey_question = SurveyQuestion.objects.order_by('qindex').first()
            answer_choices = get_answer_choices(survey_question, user.chosenLang)

            form = AnswerMChoice(answer_choices)
            form.setUID(user.user_id)
            form.set_question_id(survey_question.id)

            action = '/survey/question'
            title += " " + str(user.current_question)
            question = TranslationKey.objects.filter(lang=user.chosenLang).filter(key=survey_question.titleKey)[0].text

    else:
        form = InitialStartForm()
        form.setUID(user.user_id)

    return {
        'title': title,
        'question': question,
        'form': form,
        'action': action,
        'userId': user.user_id,
        'txtcontinuelater': TRANSLATION_UI['question']['continuelater'][user.chosenLang.lower()],
    }

def saveAndGetQuestion(user: SurveyUser, request):

    if user.survey_done:
        return -1

    survey_questions = SurveyQuestion.objects.order_by('qindex')
    survey_question = survey_questions[user.current_question - 1]
    tuple_answers = get_answer_choices(survey_question, user.chosenLang)

    # save what the answers were

    if request.method == 'POST' and user.current_question == int(request.POST['questionid']):

        form = AnswerMChoice(tuple_answers, data=request.POST)

        if form.is_valid():

            answers = form.cleaned_data['answers']
            saveAnswers(tuple_answers, answers, user)

            if user.current_question < len(survey_questions):
                user.current_question += 1
                user.save()

                survey_question = survey_questions[user.current_question - 1]
                tuple_answers = get_answer_choices(survey_question, user.chosenLang)
            else:
                #FINAL QUESTION return the new interface
                user.survey_done = True
                user.save()

                return -1

    form = AnswerMChoice(tuple_answers)
    form.setUID(user.user_id)
    form.set_question_id(survey_question.id)

    return {
        'title': "Fit4Cybersecurity - " + TRANSLATION_UI['question']['question'][user.chosenLang.lower()] + " " + str(user.current_question),
        'question': TranslationKey.objects.filter(lang=user.chosenLang).filter(key=survey_question.titleKey)[0].text,
        'form': form,
        'action': '/survey/question',
        'userId': user.user_id,
        'txtcontinuelater': TRANSLATION_UI['question']['continuelater'][user.chosenLang.lower()],
    }
        

def saveAnswers (answer_choices, answers, user):
    existinganswerids = [ int(i[0]) for i in answer_choices ]
    useranswers = [int(i) for i in answers]
    for a in existinganswerids:
        answer = SurveyUserAnswer()
        answer.user = user
        qanswer = SurveyQuestionAnswer.objects.filter(id=a)[0]
        answer.answer = qanswer
        
        answer.value = 0
        if a in useranswers:
            answer.value += 1
        
        answer.save()


def findUserById(user_id):
    return SurveyUser.objects.filter(user_id=user_id)[0]


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


def showCompleteReport(request,userID):
    cuser = SurveyUser.objects.filter(user_id=userID)[0]

    #allQuestions = SurveyQuestion.objects.all().order_by('qindex')
    allAnswers = SurveyQuestionAnswer.objects.all().order_by('question__qindex','aindex')

    #userAnswers = SurveyUserAnswer.objects.all().filter(user=cuser)

    #recommendations = Recommendations

    finalReportRecs = getRecommendations(cuser)

    allText = []
    
    for x in finalReportRecs:

        txt = x #TranslationKey.objects.filter(lang=cuser.chosenLang).filter(key=x.textKey)[0]
        #txt = txt.text.replace("\n","<br>")
        txt = txt.replace("\n","<br>")
        allText.append(str(txt))
    
    return allText
    
    # get all answers


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
    document = MailMerge(template)
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

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=result'+lang.lower()+'.docx'
    document.write(response)
    #doc.save(response)
    # make survey readonly and show results.
    # make checkboxes to recommendation and a single button of get companies
    # then call getcompanies when button is hit

    return response


def get_answer_choices(survey_question: SurveyQuestion, user_lang: str):

    tuple_answers = []

    answer_choices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=survey_question)

    for answer_choice in answer_choices:
        translation_keys = TranslationKey.objects.filter(lang=user_lang).filter(key=answer_choice.answerKey)
        if translation_keys.count() == 0:
            raise RuntimeError('The translation has to be do for the answers choices.')

        tuple_answers.append(
            (
                answer_choice.id,
                format_html(
                    '{}{}',
                    mark_safe('<span class="checkmark"></span>'),
                    translation_keys[0].text
                )
            )
        )

    return tuple_answers
