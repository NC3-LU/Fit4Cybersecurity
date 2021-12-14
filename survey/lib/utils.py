# -*- coding: utf-8 -*-

from survey.models import SurveyQuestion, SurveyQuestionAnswer, Recommendations


def export_survey(with_ids):
    """Export questions, answers, recommendations."""
    result = []
    questions = SurveyQuestion.objects.all()
    for question in questions:
        new_question = question.dump()
        new_question["answers"] = []
        if with_ids:
            new_question.update({"id": question.id})

        answers = SurveyQuestionAnswer.objects.filter(question=question).all()
        for answer in answers:
            new_answer = answer.dump()
            new_answer["recommendations"] = []
            if with_ids:
                new_answer.update({"id": answer.id})

            recommendations = Recommendations.objects.filter(forAnswer=answer).all()
            for recommendation in recommendations:
                new_recommendation = recommendation.dump()
                if with_ids:
                    new_recommendation.update({"id": recommendation.id})
                new_answer["recommendations"].append(new_recommendation)

            new_question["answers"].append(new_answer)

        result.append(new_question)

    return result
