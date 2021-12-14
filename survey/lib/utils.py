# -*- coding: utf-8 -*-

from survey.models import SurveyQuestion, SurveyQuestionAnswer, Recommendations


def export_survey():
    """Export questions, answers, recommendations."""
    result = []
    questions = SurveyQuestion.objects.all()
    for question in questions:
        new_question = question.dump()
        new_question["answers"] = []

        answers = SurveyQuestionAnswer.objects.filter(question=question).all()
        for answer in answers:
            new_answer = answer.dump()
            new_answer["recommendations"] = []

            recommendations = Recommendations.objects.filter(forAnswer=answer).all()
            for recommendation in recommendations:
                new_answer["recommendations"].append(recommendation.dump())

            new_question["answers"].append(new_answer)

        result.append(new_question)

    return result
