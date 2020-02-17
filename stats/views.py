from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from survey.models import (
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
    TranslationKey,
)


def index(request):
    return render(request, "survey/index.html")


@login_required
def get_stats(request):
    allAnswers = SurveyQuestionAnswer.objects.all().order_by(
        "question__qindex", "aindex"
    )
    for answer in allAnswers:
        userAnswer = SurveyUserAnswer.objects.filter(answer=answer)[0]
        print(userAnswer)

    return render(request, "admin/stats.html")
