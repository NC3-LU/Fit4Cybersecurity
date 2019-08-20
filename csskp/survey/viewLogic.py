from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer, SurveyUserAnswers, SurveyUserAnswer
from survey.forms import InitialStartForm, AnswerMChoice


def saveAndGetQuestion(request,id):

    tupelanswers = []

    if id <= 0:
        firstQuestion = SurveyQuestion.objects.order_by('qindex')[0]
        answerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=firstQuestion)

        for answer in answerChoices:
            tupelanswers.append( (answer.id,answer.answer) )

    # save what the answers were
    if request.method == 'POST':
        form = InitialStartForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            user=SurveyUser.objects.filter(user_id=form.cleaned_data['userid'])[0]

            # remember to save the data to the DB

            initialQuestion = InitialStartForm(form)
            
            form = AnswerMChoice(tupelanswers)
            form.setUID(user.user_id)

            question = {
                'title': "Question "+str(id+1),
                'question': firstQuestion.title,
                'form': form,
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
                tupelanswers.append( (answer.id,answer.answer) )

        form = AnswerMChoice(tupelanswers,request.POST) 

        #for answer in form.fields['answers']:
         #   print (answer + "\n")

        if form.is_valid():
            user=SurveyUser.objects.filter(user_id=form.cleaned_data['userid'])[0]

            answers = form.cleaned_data['answers']
            questionTitle = "You are done!"
            
            saveAnswers(lastAnswerChoices,answers,user)

            
            if id < len(SurveyQuestion.objects.order_by('qindex')):
                nextQuestion = SurveyQuestion.objects.order_by('qindex')[id]
                answerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=nextQuestion).order_by('aindex')
                
                

                questionTitle = nextQuestion.title

                tupelanswers.clear()

                for answer in answerChoices:
                    tupelanswers.append( (answer.id,answer.answer) )

                newform = AnswerMChoice(tupelanswers)
                newform.setUID(user.user_id)
            else:
                #FINAL QUESTION return the new interface
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
    for i in answer_choices:
        for a in answers:
            answer = SurveyUserAnswer()
            answer.user = user
            answer.answer = SurveyQuestionAnswer.objects.filter(answer=i)[0]
            
            answer.value = 0
            if int(a) == i.id:
                answer.value += 1
            
            answer.save()