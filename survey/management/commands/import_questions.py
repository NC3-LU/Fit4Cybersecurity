# -*- coding: utf-8 -*-

import json
from django.core.management.base import BaseCommand
from survey.models import (
    SurveySection,
    SurveyQuestion,
    SurveyQuestionServiceCategory,
    SurveyQuestionAnswer,
    Recommendations,
)


class Command(BaseCommand):
    help = "Import a set of questions and answers."

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="The path of the JSON file.")

    def handle(self, *args, **options):
        with open(options["json_file"]) as f:
            json_file = f.read()
        json_data = json.loads(json_file)

        nb_imported_questions = 0
        nb_imported_answers = 0
        nb_imported_recommendations = 0

        for question in json_data:
            # Get or create the section
            section, created = SurveySection.objects.get_or_create(
                label=question["section"]
            )
            if created:
                section.save()

            # Get or create the service category
            service_cat, created = SurveyQuestionServiceCategory.objects.get_or_create(
                label=question["service_category"]
            )
            if created:
                service_cat.save()

            # Before creating the question: check that the index is defined in the JSON
            # file (better to not specify indexes for your context questions).
            qindex = int(question.get("qindex", 0))
            is_context_question = question["section"] == "__context"
            if not qindex or is_context_question:
                if is_context_question:
                    # for a context question: change the index even if it is specified in
                    # the JSON
                    res = SurveyQuestion.objects.order_by("-qindex").all()
                    if res.count():
                        qindex = res[res.count() - 1].qindex - 1
                    else:
                        qindex = 1
                    qindex = -abs(qindex)
                else:
                    # normal question. Normally the index should be defined in the JSON
                    # file.
                    res = SurveyQuestion.objects.order_by("qindex").all()
                    if res.count():
                        qindex = res[res.count() - 1].qindex + 1
                    else:
                        qindex = 1

            # Create the question
            question_obj, created = SurveyQuestion.objects.get_or_create(
                label=question["label"],
                qtype=question["qtype"],
                section=section,
                service_category=service_cat,
                qindex=qindex,
                maxPoints=question["maxPoints"],
            )
            if created:
                nb_imported_questions += 1
                question_obj.save()

            # Create the answers
            answers_dependancies = {}
            for answer in question["answers"]:
                bonus_points = 0
                if "bonus_points" in answer.keys():
                    bonus_points = answer["bonus_points"]
                tooltip = ''
                if "tooltip" in answer.keys():
                    tooltip = answer["tooltip"]

                answer_obj, created = SurveyQuestionAnswer.objects.get_or_create(
                    question=question_obj,
                    label=answer["label"],
                    aindex=answer["aindex"],
                    uniqueAnswer=answer["uniqueAnswer"],
                    score=answer.get("score", 0),
                    atype=answer["atype"],
                    bonus_points=bonus_points,
                    tooltip=tooltip,
                )

                if created:
                    nb_imported_answers += 1
                    answer_obj.save()

                    # Prepare the dependencies between answers.
                    if "dependant_answers" in answer.keys():
                        answers_dependancies[answer["label"]] = {
                            "object": answer_obj,
                            "dependant_answers": answer["dependant_answers"]
                        }

                for reco in answer.get("recommendations", []):
                    reco_obj, created = Recommendations.objects.get_or_create(
                        label=reco["label"],
                        min_e_count=reco["min_e_count"],
                        max_e_count=reco["max_e_count"],
                        sector=reco["sector"],
                        forAnswer=answer_obj,
                        answerChosen=reco["answerChosen"],
                    )
                    if created:
                        nb_imported_recommendations += 1
                        reco_obj.save()

            # Process the answers' dependencies.
            for answer_label in answers_dependancies:
                question_answer = answers_dependancies[answer_label]["object"]
                dependant_answers_labels = answers_dependancies[answer_label]["dependant_answers"]
                for dependant_answer_label in dependant_answers_labels:
                    question_answer.dependant_answers.add(
                        answers_dependancies[dependant_answer_label]['object'])
                    question_answer.save()
                    answers_dependancies[dependant_answer_label]['object'].dependant_answers.add(
                        question_answer)
                    answers_dependancies[dependant_answer_label]['object'].save()

        self.stdout.write(self.style.SUCCESS("Data imported."))
        self.stdout.write(
            self.style.SUCCESS(
                "  Number of questions: {}".format(nb_imported_questions)
            )
        )
        self.stdout.write(
            self.style.SUCCESS("  Number of answers: {}".format(nb_imported_answers))
        )
        self.stdout.write(
            self.style.SUCCESS(
                "  Number of recommendations: {}".format(nb_imported_recommendations)
            )
        )
