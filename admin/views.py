# -*- coding: utf-8 -*-

from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from survey.models import SurveyQuestion, Translation


def tree():
    return defaultdict(tree)


@login_required
def translations_questions(request):
    questions = SurveyQuestion.objects.all()
    translations_query = Translation.objects
    paginator = Paginator(questions, 20)  # Show 20 questions per page.
    translations = tree()
    for translation in translations_query.all():
        translations[translation.original][translation.lang] = translation.translated

    to_translate = []
    for question in questions:
        if question.label not in translations.keys():
            to_translate.append(question)
        else:
            if (
                "de" not in translations[question.label].keys()
                or "fr" not in translations[question.label].keys()
            ):
                to_translate.append(question)

    page_number = request.GET.get("page")
    paginated_questions = paginator.get_page(page_number)
    return render(
        request,
        "admin/translations.html",
        {
            "nb_questions": len(questions),
            "to_translate": to_translate,
            "questions": paginated_questions,
            "translations": translations,
            "languages": ["fr", "de"],
        },
    )
