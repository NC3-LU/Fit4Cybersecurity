# -*- coding: utf-8 -*-

import json
from typing import Dict, List
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

            # For a context question: change the index even if it is specified in
            # the JSON
            qindex = int(question.get("qindex", 1))
            is_context_question = question["section"] == "__context"
            if is_context_question:
                res = SurveyQuestion.objects.order_by("-qindex").filter(
                    section__label__contains="__context"
                )
                if self.does_question_exists(question["label"], res):
                    continue
                # if res.count() is 0, qindex is 1
                qindex = res[res.count() - 1].qindex - 1 if res.count() else qindex
                qindex = -abs(qindex)

            # Create the question
            question_obj, created = SurveyQuestion.objects.get_or_create(
                label=question["label"],
                qtype=question["qtype"],
                section=section,
                service_category=service_cat,
                qindex=qindex,
                maxPoints=question["maxPoints"],
                answers_order=question.get("answers_order", "aindex"),
            )
            if created:
                nb_imported_questions += 1
                question_obj.save()

            # Create the answers
            answers_dependencies = {}
            for answer in question["answers"]:
                answer_obj, created = SurveyQuestionAnswer.objects.get_or_create(
                    question=question_obj,
                    label=answer["label"],
                    aindex=answer["aindex"],
                    uniqueAnswer=answer["uniqueAnswer"],
                    score=answer.get("score", 0),
                    atype=answer["atype"],
                    bonus_points=int(answer.get("bonus_points", 0)),
                    tooltip=answer.get("tooltip", ""),
                )

                if created:
                    nb_imported_answers += 1
                    answer_obj.save()

                    # Prepare the dependencies between answers.
                    if "dependant_answers" in answer.keys():
                        answers_dependencies[answer["label"]] = {
                            "object": answer_obj,
                            "dependant_answers": answer["dependant_answers"],
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
            self.process_answers_dependencies(answers_dependencies)

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

    @staticmethod
    def does_question_exists(label: str, questions: List[SurveyQuestion]):
        return label in [question.label for question in questions]

    @staticmethod
    def process_answers_dependencies(answers_dependencies: Dict):
        for answer_label in answers_dependencies:
            question_answer = answers_dependencies[answer_label]["object"]
            dependant_answers_labels = answers_dependencies[answer_label][
                "dependant_answers"
            ]
            for dependant_answer_label in dependant_answers_labels:
                question_answer.dependant_answers.add(
                    answers_dependencies[dependant_answer_label]["object"]
                )
                question_answer.save()
                answers_dependencies[dependant_answer_label][
                    "object"
                ].dependant_answers.add(question_answer)
                answers_dependencies[dependant_answer_label]["object"].save()
