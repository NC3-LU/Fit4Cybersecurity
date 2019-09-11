from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer, SurveyUserAnswer, TranslationKey
from survey.forms import InitialStartForm, AnswerMChoice
from survey.globals import LANG_SELECT


def saveAndGetQuestion(request,id):
    try:
        userLang=request.session['lang']
        if userLang not in [x[0] for x in LANG_SELECT]:
            return None
    except:
        return None

    tupelanswers = []

    user=SurveyUser.objects.filter(user_id=request.session['user_id'])[0]
    if user.chosenLang != userLang:
        user.chosenLang = userLang
        user.save()
        
    firstQuestion = SurveyQuestion.objects.order_by('qindex')[0]
    answerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=firstQuestion)

    for answer in answerChoices:
        tupelanswers.append( (answer.id,TranslationKey.objects.filter(lang=userLang).filter(key=answer.answerKey)[0].text) )
    

    # save what the answers were
    if request.method == 'POST':
        form = InitialStartForm(data=request.POST) # A form bound to the POST data
        if form.is_valid():
            
            if id <= 0:
                id = 0

            user.sector = form.cleaned_data['sector']
            user.e_count = form.cleaned_data['compSize']
            user.current_question = id
            user.save()

            qform = AnswerMChoice(tupelanswers)
            qform.setUID(user.user_id)

            question = {
                'title': "Question "+str(id+1),
                'question': TranslationKey.objects.filter(lang=user.chosenLang).filter(key=firstQuestion.titleKey)[0].text,
                'form': qform,
                'next': id+1,
                'user': user.user_id,
            }

            return question
        
        lastQuestion = ""
        lastAnswerChoices = ""

        

        if id > 0:
            lastQuestion = SurveyQuestion.objects.order_by('qindex')[id-1]
            lastAnswerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=lastQuestion)

            tupelanswers.clear()

            for answer in lastAnswerChoices:
                tupelanswers.append( (answer.id,TranslationKey.objects.filter(lang=user.chosenLang).filter(key=answer.answerKey)[0].text) )

        form = AnswerMChoice(tupelanswers,data=request.POST) 

        #for answer in form.fields['answers']:
         #   print (answer + "\n")

        if form.is_valid():

            answers = form.cleaned_data['answers']
            questionTitle = "You are done!"
            
            saveAnswers(lastAnswerChoices,answers,user)

            
            if id < len(SurveyQuestion.objects.order_by('qindex')):
                user.current_question = id
                user.save()

                nextQuestion = SurveyQuestion.objects.order_by('qindex')[id]
                answerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=nextQuestion).order_by('aindex')

                questionTitle = TranslationKey.objects.filter(lang=user.chosenLang).filter(key=nextQuestion.titleKey)[0].text

                tupelanswers.clear()

                for answer in answerChoices:
                    tupelanswers.append( (answer.id,TranslationKey.objects.filter(lang=user.chosenLang).filter(key=answer.answerKey)[0].text) )

                newform = AnswerMChoice(tupelanswers)
                newform.setUID(user.user_id)
            else:
                #FINAL QUESTION return the new interface
                user.current_question = id
                user.survey_done = True
                user.save()
                return -1

            # GET THE QUESTIONS FROM DB
            question = {
                'title': "Question "+str(id+1),
                'question': questionTitle,
                'form': newform,
                'next': id+1,
                'user': user.user_id,
            }
 
            return question
        
        return {'question':form.errors}

    return None



def saveAnswers (answer_choices,answers,user):
    existinganswerids = [ int(i.id) for i in answer_choices ]
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
