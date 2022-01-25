# -*- coding: utf-8 -*-

from collections import defaultdict
from survey.models import SurveyQuestion, SurveyQuestionAnswer, Recommendations


def tree():
    """Autovivification."""
    return defaultdict(tree)


def mean_list(list):
    return sum(list) / len(list)


def mean_gen():
    """Yields the accumulated mean of sent values.
    >>> g = mean_gen()
    >>> g.send(None) # Initialize the generator
    >>> g.send(4)
    4.0
    >>> g.send(10)
    7.0
    >>> g.send(-2)
    4.0
    """
    sum = yield (None)
    count = 1
    while True:
        try:
            sum += yield (sum / float(count))
            count += 1
        except Exception:
            yield sum


def export_survey(with_ids=False):
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
