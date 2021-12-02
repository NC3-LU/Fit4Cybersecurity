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

            # Create the question
            question_obj, created = SurveyQuestion.objects.get_or_create(
                label=question["label"],
                qtype=question["qtype"],
                section=section,
                service_category=service_cat,
                qindex=question["qindex"],
                maxPoints=question["maxPoints"],
            )
            if created:
                nb_imported_questions += 1
                question_obj.save()

            # Create the answers
            for answer in question["answers"]:
                bonus_points = 0
                if bonus_points in answer:
                    answer["bonus_points"] = answer["bonus_points"]
                answer_obj, created = SurveyQuestionAnswer.objects.get_or_create(
                    question=question_obj,
                    label=answer["label"],
                    aindex=answer["aindex"],
                    uniqueAnswer=answer["uniqueAnswer"],
                    score=answer["score"],
                    atype=answer["atype"],
                    bonus_points=bonus_points
                )
                if created:
                    nb_imported_answers += 1
                    answer_obj.save()

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
