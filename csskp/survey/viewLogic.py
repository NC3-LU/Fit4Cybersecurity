from survey.models import SurveyUser
from survey.forms import InitialStartForm, AnswerMChoice


def saveAndGetQuestion(request,id):


    # CHANGE THIS to info from DB
    answer_list = [
        'james',
        'marc',
        'michael',
        'peter',
        'tim',
    ]
    
    tupelanswers = []
    i=0
    for a in answer_list:
        tupelanswers.append( (i,a) )
        i+=1
    # END CHANGE THIS

    # save what the answers were
    if request.method == 'POST':
        form = InitialStartForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            user=form.cleaned_data['userid']

            # remember to save the data to the DB

            
            
            form = AnswerMChoice(tupelanswers)
            form.setUID(user)

            question = {
                'title': "Question "+str(id),
                'question': "Who are you?",
                'form': form,
                'next': id+1,
            }

            return question


        form = AnswerMChoice(tupelanswers,request.POST)        
        if form.is_valid():
            user=form.cleaned_data['userid']

            question = {
                'title': "Question "+str(id),
                'question': "Who are you?",
                'form': form,
                'next': id+1,
            }

            return question
        
        return {'question':form.errors}


    return None