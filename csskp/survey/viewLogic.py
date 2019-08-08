from survey.models import SurveyUser, SurveyQuestion, SurveyQuestionAnswer
from survey.forms import InitialStartForm, AnswerMChoice


def saveAndGetQuestion(request,id):

    tupelanswers = []
    i=0

    if id <= 0:
        firstQuestion = SurveyQuestion.objects.all()[0]
        answerChoices = SurveyQuestionAnswer.objects.filter(question=firstQuestion)

        for answer in answerChoices:
            tupelanswers.append( (i,answer.answer) )
            i+=1

    # save what the answers were
    if request.method == 'POST':
        form = InitialStartForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            user=form.cleaned_data['userid']

            # remember to save the data to the DB

            
            
            form = AnswerMChoice(tupelanswers)
            form.setUID(user)

            question = {
                'title': "Question "+str(id+1),
                'question': firstQuestion.title,
                'form': form,
                'next': id+1,
            }

            return question
        
        if id > 0:
            lastQuestion = SurveyQuestion.objects.all()[id-1]
            answerChoices = SurveyQuestionAnswer.objects.filter(question=lastQuestion)

            tupelanswers.clear()
            i=0

            for answer in answerChoices:
                tupelanswers.append( (i,answer.answer) )
                i+=1

        form = AnswerMChoice(tupelanswers,request.POST)        
        if form.is_valid():
            user=form.cleaned_data['userid']
            questionTitle = "You are done!"

            if id < len(SurveyQuestion.objects.all()):
                nextQuestion = SurveyQuestion.objects.all()[id]
                answerChoices = SurveyQuestionAnswer.objects.filter(question=nextQuestion)
                
                questionTitle = nextQuestion.title

                tupelanswers.clear()
                i=0

                for answer in answerChoices:
                    tupelanswers.append( (i,answer.answer) )
                    i+=1

                newform = AnswerMChoice(tupelanswers)
                newform.setUID(user)
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