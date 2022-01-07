# -*- coding: utf-8 -*-

import json
from typing import Dict, List
from django.core.management.base import BaseCommand
from django.db.models import Max
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
        nb_updated_questions = 0
        nb_imported_answers = 0
        nb_updated_answers = 0
        nb_imported_recommendations = 0
        max_question_index = 0

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

            # The context questions have negative indexes.
            qindex = int(question.get("qindex", 1))
            qindex = abs(qindex) if question["section"] != "__context" else -abs(qindex)

            if qindex > max_question_index:
                max_question_index = qindex

            # Create or update the question
            try:
                question_obj = SurveyQuestion.objects.get(qindex=qindex)
                question_obj.label = question["label"]
                question_obj.qtype = question["qtype"]
                question_obj.section = section
                question_obj.service_category = service_cat
                question_obj.maxPoints = question["maxPoints"]
                question_obj.answers_order = question.get("answers_order", "aindex")
                question_obj.is_active = True

                question_obj.save()
                nb_updated_questions += 1
            except SurveyQuestion.DoesNotExist as e:
                question_obj = SurveyQuestion.objects.create(
                    label=question["label"],
                    qtype=question["qtype"],
                    section=section,
                    service_category=service_cat,
                    qindex=qindex,
                    maxPoints=question["maxPoints"],
                    answers_order=question.get("answers_order", "aindex"),
                    is_active=True,
                )

                nb_imported_questions += 1

            # Countries list (CL) is a special django_countries.CountryField filed type.
            if question_obj.qtype == 'CL':
                continue

            # Create the answers
            answers_dependencies = {}
            for answer in question["answers"]:
                try:
                    answer_obj = SurveyQuestionAnswer.objects.get(
                        question=question_obj,
                        aindex=answer["aindex"]
                    )
                    answer_obj.label = answer["label"]
                    answer_obj.value = answer.get("value", ""),
                    answer_obj.uniqueAnswer = answer["uniqueAnswer"]
                    answer_obj.score = answer.get("score", 0)
                    answer_obj.atype = answer["atype"]
                    answer_obj.bonus_points = int(answer.get("bonus_points", 0))
                    answer_obj.tooltip = answer.get("tooltip", "")
                    answer_obj.is_active = True

                    answer_obj.save()
                    is_answer_created = True
                    nb_updated_answers += 1
                except SurveyQuestionAnswer.DoesNotExist as e:
                    answer_obj = SurveyQuestionAnswer.objects.create(
                        question=question_obj,
                        label=answer["label"],
                        value=answer.get("value", None),
                        aindex=answer["aindex"],
                        uniqueAnswer=answer["uniqueAnswer"],
                        score=answer.get("score", 0),
                        atype=answer["atype"],
                        bonus_points=int(answer.get("bonus_points", 0)),
                        tooltip=answer.get("tooltip", ""),
                        is_active=True,
                    )
                    nb_imported_answers += 1
                    is_answer_created = False

                # Clean all the dependant answers and recommendations to recreate later.
                if not is_answer_created:
                    answer_obj.dependant_answers.clear()
                    Recommendations.objects.filter(
                        forAnswer=answer_obj
                    ).delete()

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

            # Deactivate all the answers with index higher then max importing.
            max_answer_index = max(question["answers"], key=lambda x: x["aindex"])
            if max_answer_index:
                SurveyQuestionAnswer.objects.filter(
                    question=question_obj,
                    aindex__gt=max_answer_index["aindex"]
                ).update(is_active=False)

            # Process the answers' dependencies.
            self.process_answers_dependencies(answers_dependencies)

        # Deactivate all the questions with index higher then max importing.
        if max_question_index:
            SurveyQuestion.objects.filter(
                qindex__gt=max_question_index
            ).update(is_active=False)

        self.stdout.write(self.style.SUCCESS("Data imported."))
        self.stdout.write(
            self.style.SUCCESS(
                "  Number of created questions: {}".format(nb_imported_questions)
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "  Number of updated questions: {}".format(nb_updated_questions)
            )
        )
        self.stdout.write(
            self.style.SUCCESS("  Number of created answers: {}".format(nb_imported_answers))
        )
        self.stdout.write(
            self.style.SUCCESS(
                "  Number of updated answers: {}".format(nb_updated_answers)
            )
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
