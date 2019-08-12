from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer
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
            }

            return question
        
        if id > 0:
            lastQuestion = SurveyQuestion.objects.order_by('qindex')[id-1]
            answerChoices = SurveyQuestionAnswer.objects.order_by('aindex').filter(question=lastQuestion)

            tupelanswers.clear()

            for answer in answerChoices:
                tupelanswers.append( (answer.id,answer.answer) )

        form = AnswerMChoice(tupelanswers,request.POST)        
        if form.is_valid():
            user=SurveyUser.objects.filter(user_id=form.cleaned_data['userid'])[0]
            questionTitle = "You are done!"

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
            }

            return question
        
        return {'question':form.errors}


    return None