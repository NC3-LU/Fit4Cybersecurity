import json
from typing import Dict
from typing import List

from django.core.management.base import BaseCommand

from survey.models import CONTEXT_SECTION_LABEL
from survey.models import Recommendations
from survey.models import SurveyAnswerQuestionMap
from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer
from survey.models import SurveyQuestionAnswerScore
from survey.models import SurveyQuestionMaxScore
from survey.models import SurveyQuestionServiceCategory
from survey.models import SurveySection


class Command(BaseCommand):
    help = "Import a set of questions and answers."

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="The path of the JSON file.")

    def handle(self, *args, **options):  # noqa: C901
        with open(options["json_file"]) as f:
            json_file = f.read()
        json_data = json.loads(json_file)

        nb_imported_questions = 0
        nb_updated_questions = 0
        nb_imported_answers = 0
        nb_updated_answers = 0
        nb_imported_recommendations = 0

        max_question_index = 0
        min_question_index = 0

        answers_questions_map = {}
        answers_to_remove_map = []

        questions_max_scores = {}
        answers_scores = {}

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
            qindex = (
                abs(qindex)
                if question["section"] != CONTEXT_SECTION_LABEL
                else -abs(qindex)
            )

            if qindex > max_question_index:
                max_question_index = qindex
            if qindex < min_question_index:
                min_question_index = qindex

            # Create or update the question
            try:
                question_obj = SurveyQuestion.all_objects.get(qindex=qindex)
                question_obj.label = question["label"]
                question_obj.qtype = question["qtype"]
                question_obj.section = section
                question_obj.service_category = service_cat
                question_obj.maxPoints = question.get("maxPoints", 0)
                question_obj.answers_order = question.get("answers_order", "aindex")
                question_obj.is_active = True

                question_obj.save()

                # Prepare max_scores dependency for SurveyQuestionMaxScore.
                if "max_scores" in question.keys():
                    questions_max_scores[question_obj.id] = []
                    for max_score_data in question["max_scores"]:
                        questions_max_scores[question_obj.id].append(
                            {
                                "question": question_obj,
                                "question_of_answer": max_score_data[
                                    "question_of_answer"
                                ],
                                "selected_answer": max_score_data["selected_answer"],
                                "max_score": max_score_data["max_score"],
                            }
                        )

                nb_updated_questions += 1
            except SurveyQuestion.DoesNotExist:
                question_obj = SurveyQuestion.objects.create(
                    label=question["label"],
                    qtype=question["qtype"],
                    section=section,
                    service_category=service_cat,
                    qindex=qindex,
                    maxPoints=question.get("maxPoints", 0),
                    answers_order=question.get("answers_order", "aindex"),
                    is_active=True,
                )

                nb_imported_questions += 1

            # Create the answers
            answers_dependencies = {}
            for answer in question["answers"]:
                try:
                    answer_obj = SurveyQuestionAnswer.all_objects.get(
                        question=question_obj, aindex=answer["aindex"]
                    )
                    answer_obj.label = answer["label"]
                    answer_obj.value = answer.get("value", None)
                    answer_obj.uniqueAnswer = answer["uniqueAnswer"]
                    answer_obj.score = answer.get("score", 0)
                    answer_obj.atype = answer["atype"]
                    answer_obj.bonus_points = int(answer.get("bonus_points", 0))
                    answer_obj.tooltip = answer.get("tooltip", "")
                    answer_obj.is_active = True

                    answer_obj.save()
                    is_answer_created = False
                    nb_updated_answers += 1
                except SurveyQuestionAnswer.DoesNotExist:
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
                    is_answer_created = True

                # Clean all the dependant answers and recommendations to recreate later.
                if not is_answer_created:
                    answer_obj.dependant_answers.clear()
                    Recommendations.objects.filter(forAnswer=answer_obj).delete()

                # Prepare the dependencies between answers.
                if "dependant_answers" in answer.keys():
                    answers_dependencies[answer["label"]] = {
                        "object": answer_obj,
                        "dependant_answers": answer["dependant_answers"],
                    }

                # Prepare the answer -> questions map
                if "questions_map" in answer.keys():
                    answers_questions_map[answer_obj.id] = {
                        "object": answer_obj,
                        "questions_map": answer["questions_map"],
                    }
                else:
                    answers_to_remove_map.append(answer_obj)

                for reco in answer.get("recommendations", []):
                    categories = []
                    if "categories" in reco:
                        for reco_category in reco["categories"]:
                            (
                                reco_cat,
                                created,
                            ) = SurveyQuestionServiceCategory.objects.get_or_create(
                                label=reco_category["label"]
                            )
                            if created:
                                reco_cat.save()
                            categories.append(reco_cat)
                    reco_obj, created = Recommendations.objects.get_or_create(
                        label=reco["label"],
                        min_e_count=reco.get("min_e_count", "a"),
                        max_e_count=reco.get("max_e_count", "z"),
                        sector=reco.get("sector", None),
                        forAnswer=answer_obj,
                        answerChosen=reco["answerChosen"],
                    )
                    for category in categories:
                        reco_obj.categories.add(category)
                    if created:
                        nb_imported_recommendations += 1
                        reco_obj.save()

                # Prepare scores dependency for SurveyQuestionAnswerScore.
                if "scores" in answer.keys():
                    answers_scores[answer_obj.id] = []
                    for score_data in answer["scores"]:
                        answers_scores[answer_obj.id].append(
                            {
                                "answer": answer_obj,
                                "question_of_answer": score_data["question_of_answer"],
                                "selected_answer": score_data["selected_answer"],
                                "score": score_data["score"],
                            }
                        )

            # Deactivate all the answers with index higher then max importing.
            max_answer_index = max(question["answers"], key=lambda x: x["aindex"])
            if max_answer_index:
                SurveyQuestionAnswer.all_objects.filter(
                    question=question_obj, aindex__gt=max_answer_index["aindex"]
                ).update(is_active=False)

            # Process the answers' dependencies.
            self.process_answers_dependencies(answers_dependencies)

        # Process the answers -> questions map populated before.
        self.process_answers_questions_map(answers_questions_map, answers_to_remove_map)

        # Deactivate all the questions with index higher then max importing.
        if max_question_index:
            SurveyQuestion.all_objects.filter(qindex__gt=max_question_index).update(
                is_active=False
            )
        # Deactivate all the questions with lower index (for context questions).
        if min_question_index:
            SurveyQuestion.all_objects.filter(qindex__lt=min_question_index).update(
                is_active=False
            )

        # Handle the questions max_scores and answers scores dependencies.
        if len(questions_max_scores) > 0 and len(answers_scores) > 0:
            self.process_questions_answers_scores_dependencies(
                questions_max_scores, answers_scores
            )

        self.stdout.write(self.style.SUCCESS("Data imported."))
        self.stdout.write(
            self.style.SUCCESS(
                f"  Number of created questions: {nb_imported_questions}"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(f"  Number of updated questions: {nb_updated_questions}")
        )
        self.stdout.write(
            self.style.SUCCESS(f"  Number of created answers: {nb_imported_answers}")
        )
        self.stdout.write(
            self.style.SUCCESS(f"  Number of updated answers: {nb_updated_answers}")
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"  Number of recommendations: {nb_imported_recommendations}"
            )
        )

    @staticmethod
    def process_answers_dependencies(answers_dependencies: Dict) -> None:
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

    @staticmethod
    def process_answers_questions_map(
        answers_questions_map: Dict, answers_to_remove_map: List[SurveyQuestionAnswer]
    ) -> None:
        SurveyAnswerQuestionMap.objects.filter(
            answer__in=answers_to_remove_map
        ).delete()
        for answer_id in answers_questions_map:
            answer = answers_questions_map[answer_id]["object"]
            SurveyAnswerQuestionMap.objects.filter(answer=answer).delete()
            answer_questions_map = answers_questions_map[answer_id]["questions_map"]
            for answer_question_map in answer_questions_map:
                question = SurveyQuestion.objects.get(
                    label=answer_question_map["label"]
                )
                SurveyAnswerQuestionMap.objects.create(
                    answer=answer,
                    question=question,
                    branch=answer_question_map["branch"],
                    level=answer_question_map["level"],
                    order=answer_question_map["order"],
                )

    @staticmethod
    def process_questions_answers_scores_dependencies(
        questions_max_scores: Dict, answers_scores: Dict
    ) -> None:
        SurveyQuestionMaxScore.objects.all().delete()
        SurveyQuestionAnswerScore.objects.all().delete()
        for question_id in questions_max_scores:
            for question_max_score in questions_max_scores[question_id]:
                selected_answer = SurveyQuestionAnswer.objects.filter(
                    question__label=question_max_score["question_of_answer"],
                    label=question_max_score["selected_answer"],
                )[:1][0]
                SurveyQuestionMaxScore.objects.create(
                    question=question_max_score["question"],
                    selected_answer=selected_answer,
                    max_score=question_max_score["max_score"],
                )
        for answer_id in answers_scores:
            for answer_score in answers_scores[answer_id]:
                selected_answer = SurveyQuestionAnswer.objects.filter(
                    question__label=answer_score["question_of_answer"],
                    label=answer_score["selected_answer"],
                )[:1][0]
                SurveyQuestionAnswerScore.objects.create(
                    answer=answer_score["answer"],
                    selected_answer=selected_answer,
                    score=answer_score["score"],
                )
