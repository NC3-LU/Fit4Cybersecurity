from django.http import HttpResponse
from django.utils.html import format_html, mark_safe

from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer, SurveyUserAnswer, TranslationKey
from survey.forms import InitialStartForm, AnswerMChoice
from survey.globals import LANG_SELECT, TRANSLATION_UI
from survey.reporthelper import getRecommendations
#from utils.radarFactory import radar_factory
#import matplotlib.pyplot as plt


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
                form = AnswerMChoice(tuple_answers)
            else:
                #FINAL QUESTION return the new interface
                user.survey_done = True
                user.save()

                return -1
    else:
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


def showCompleteReport(request, userID):
    cuser = SurveyUser.objects.filter(user_id=userID)[0]

    # allQuestions = SurveyQuestion.objects.all().order_by('qindex')
    allAnswers = SurveyQuestionAnswer.objects.all().order_by('question__qindex', 'aindex')

    # userAnswers = SurveyUserAnswer.objects.all().filter(user=cuser)

    # recommendations = Recommendations

    finalReportRecs = getRecommendations(cuser)

    allText = []

    for x in finalReportRecs:
        txt = x  # TranslationKey.objects.filter(lang=cuser.chosenLang).filter(key=x.textKey)[0]
        # txt = txt.text.replace("\n","<br>")
        txt = txt.replace("\n", "<br>")
        allText.append(str(txt))

    return allText

    # get all answers


def createAndSendReport(request, userID, lang):
    from mailmerge import MailMerge
    from datetime import date
    from docx import Document
    from docx.shared import Cm, Inches

    cuser = SurveyUser.objects.filter(user_id=userID)[0]

    filepath = 'wtemps/'

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


def example_data():
    # The following data is from the Denver Aerosol Sources and Health study.
    # See doi:10.1016/j.atmosenv.2008.12.017
    #
    # The data are pollution source profile estimates for five modeled
    # pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
    # species. The radar charts are experimented with here to see if we can
    # nicely visualize how the modeled source profiles change across four
    # scenarios:
    #  1) No gas-phase species present, just seven particulate counts on
    #     Sulfate
    #     Nitrate
    #     Elemental Carbon (EC)
    #     Organic Carbon fraction 1 (OC)
    #     Organic Carbon fraction 2 (OC2)
    #     Organic Carbon fraction 3 (OC3)
    #     Pyrolized Organic Carbon (OP)
    #  2)Inclusion of gas-phase specie carbon monoxide (CO)
    #  3)Inclusion of gas-phase specie ozone (O3).
    #  4)Inclusion of both gas-phase species is present...
    data = [
        ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
        ('Basecase', [
            [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
            [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
            [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]]),
        ('With CO', [
            [0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
            [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
            [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
            [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
            [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]]),
        ('With O3', [
            [0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
            [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
            [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
            [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
            [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]]),
        ('CO & O3', [
            [0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
            [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
            [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
            [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
            [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]])
    ]
    return data


def generate_chart_png(user_id: str):
    n = 9
    theta = radar_factory(n, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, axes = plt.subplots(figsize=(9, 9), nrows=2, ncols=2,
                             subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    # Plot the four cases from the example data on separate axes
    for ax, (title, case_data) in zip(axes.flat, data):
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    ax = axes[0, 0]
    labels = ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
    legend = ax.legend(labels, loc=(0.9, .95),
                       labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    file_name = './static/users/survey-' + user_id + '.png'
    plt.savefig(file_name)

    return file_name.lstrip('.')
