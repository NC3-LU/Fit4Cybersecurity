from django.utils.html import format_html, mark_safe

from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer, SurveyUserAnswer, TranslationKey, SURVEY_STATUS_PREVIEW, SURVEY_STATUS_FINISHED
from survey.forms import InitialStartForm, AnswerMChoice
from survey.globals import LANG_SELECT, TRANSLATION_UI
from survey.reporthelper import getRecommendations, get_formatted_translations


def create_user(lang: str, sector: str, company_size: str):
    user = SurveyUser()
    user.sector = sector
    user.e_count = company_size
    survey_question = SurveyQuestion.objects.order_by('qindex')[:1]
    user.current_qindex = survey_question[0].qindex

    # prevent the use of custom languages
    langs = [x[0] for x in LANG_SELECT]
    if lang in langs:
        user.chosenLang = lang
    else:
        user.chosenLang = LANG_SELECT[0][0]

    user.save()

    return user


def handle_start_survey(request, lang: str):
    action = '/survey/start/' + lang
    question = TRANSLATION_UI['question']['description'][lang.lower()]
    title = "Fit4Cybersecurity - " + TRANSLATION_UI['question']['title'][lang.lower()]

    if request.method == 'POST':
        form = InitialStartForm(data=request.POST, lang=lang)

        if form.is_valid():
            user = create_user(lang, form.cleaned_data['sector'], form.cleaned_data['compSize'])

            request.session['lang'] = lang
            request.session['user_id'] = str(user.user_id)

            return user
    else:
        form = InitialStartForm(lang=lang)

    return {
        'title': title,
        'question': question,
        'form': form,
        'action': action,
    }


def handle_question_answers_request(request, user: SurveyUser, question_index: int):
    previous_question, current_question, next_question, total_questions_num = get_questions_slice(question_index)

    try:
        tuple_answers = get_answer_choices(current_question, user.chosenLang)
    except Exception as e:
        raise e

    if request.method == 'POST':
        form = AnswerMChoice(tuple_answers, data=request.POST,
                     lang=user.chosenLang, answers_field_type=current_question.qtype)

        if form.is_valid():

            answers = form.cleaned_data['answers']
            save_answers(tuple_answers, answers, user)

            if next_question != None:
                user.current_qindex = next_question.qindex
            else:
                user.status = SURVEY_STATUS_PREVIEW

            user.save()

            return None
    else:
        user_answers = SurveyUserAnswer.objects.filter(user=user, answer__question=current_question, uvalue__gt=0)
        selected_answers = []
        for user_answer in user_answers:
            selected_answers.append(user_answer.answer.id)

        form = AnswerMChoice(tuple_answers, lang=user.chosenLang, answers_field_type=current_question.qtype)
        form.set_answers(selected_answers)

    form.setUID(user.user_id)

    uniqueAnswers = SurveyQuestionAnswer.objects.filter(question=current_question, uniqueAnswer=True)
    uniqueAnswers = ','.join(str(uniqueAnswer.id) for uniqueAnswer in uniqueAnswers)
    form.set_unique_answers(uniqueAnswers)

    return {
        'title': "Fit4Cybersecurity - " + TRANSLATION_UI['question']['question'][user.chosenLang.lower()] + " " + str(current_question.qindex),
        'question': TranslationKey.objects.filter(lang=user.chosenLang).filter(key=current_question.titleKey)[0].text,
        'form': form,
        'action': '/survey/question/' + str(current_question.qindex),
        'user': user,
        'current_question_index': current_question.qindex,
        'previous_question_index': previous_question.qindex,
        'total_questions_num': total_questions_num,
    }


def save_answers(answer_choices, answers, user):
    existing_answer_ids = [int(i[0]) for i in answer_choices]
    user_answers = [int(i) for i in answers]
    for a in existing_answer_ids:
        answer = SurveyUserAnswer.objects.filter(user=user, answer__id=a)
        if not answer:
            answer = SurveyUserAnswer()
            answer.user = user
        else:
            answer = answer[0]

        qanswer = SurveyQuestionAnswer.objects.filter(id=a)[0]
        answer.answer = qanswer

        answer.uvalue = 0
        if a in user_answers:
            answer.uvalue = 1

        answer.save()


def find_user_by_id(user_id):
    return SurveyUser.objects.filter(user_id=user_id)[0]


def get_answer_choices(survey_question: SurveyQuestion, user_lang: str):
    tuple_answers = []
    answer_choices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=survey_question)

    for answer_choice in answer_choices:
        translation_key = TranslationKey.objects.filter(lang=user_lang, key=answer_choice.answerKey)
        if translation_key.count() == 0:
            raise Exception('The translation has to be done for the answers choices. ' +
                'Please choose an another language.')

        tuple_answers.append(
            (
                answer_choice.id,
                format_html(
                    '{}{}',
                    mark_safe('<span class="checkmark"></span>'),
                    translation_key[0].text
                )
            )
        )

    return tuple_answers


def get_questions_slice(question_index: int):
    survey_questions = SurveyQuestion.objects.order_by('qindex')
    total_questions_num = len(survey_questions)
    previous_question = survey_questions[0]
    next_question = None
    current_element_index = 0
    for survey_question in survey_questions:
        if question_index == survey_question.qindex:
            current_question = survey_question
            if current_element_index + 1 < total_questions_num:
                next_question = survey_questions[current_element_index + 1]
            break
        previous_question = survey_question
        current_element_index += 1

    return previous_question, current_question, next_question, total_questions_num


def get_questions_with_user_answers(user: SurveyUser):
    survey_user_answers = SurveyUserAnswer.objects.filter(user=user).order_by('answer__question__qindex', 'answer__aindex')
    questions_translations = get_formatted_translations(user.chosenLang, 'Q')
    answers_translations = get_formatted_translations(user.chosenLang, 'A')

    questions_with_user_answers = {}
    for survey_user_answer in survey_user_answers:
        question_title = questions_translations[survey_user_answer.answer.question.titleKey]
        question_index = survey_user_answer.answer.question.qindex
        if question_index not in questions_with_user_answers:
            questions_with_user_answers[question_index] = {'question_title': question_title, 'user_answers': []}

        questions_with_user_answers[question_index]['user_answers'].append({
            'value': survey_user_answer.uvalue,
            'title': answers_translations[survey_user_answer.answer.answerKey],
        })

    return questions_with_user_answers
