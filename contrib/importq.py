# -*- coding: utf-8 -*-

"""importq.py - Generate JSON files with the output of the command:

$ python manage.py dumpdata --indent 2 survey > ./contrib/out.json
Based on the old structure of the Fit4Cybersecurity database.

importq.py will create two files:
- questions.json
- translations.json

Those can be imported in your instance:
$ python manage.py import_questions contrib/questions.json
$ python manage.py import_translations contrib/translations.json
"""

import json

with open("out.json") as f:
    data = json.loads(f.read())

sections = [elem for elem in data if elem["model"] == "survey.surveysection"]
categories = [
    elem for elem in data if elem["model"] == "survey.surveyquestionservicecategory"
]
questions = [elem for elem in data if elem["model"] == "survey.surveyquestion"]
answers = [elem for elem in data if elem["model"] == "survey.surveyquestionanswer"]
recommendations = [elem for elem in data if elem["model"] == "survey.recommendations"]
translations = [elem for elem in data if elem["model"] == "survey.translationkey"]


questions_json = []
for question in questions:

    new_question = question["fields"]

    # Related answers
    related_answers = [
        answer for answer in answers if answer["fields"]["question"] == question["pk"]
    ]
    # Related category
    related_category = [
        category
        for category in categories
        if category["pk"] == question["fields"]["service_category"]
    ][0]
    # Related section
    related_section = [
        section
        for section in sections
        if section["pk"] == question["fields"]["section"]
    ][0]

    new_question["answers"] = []
    for answer in related_answers:
        # Related recommendations
        related_recommendations = [
            recommendation["fields"]
            for recommendation in recommendations
            if recommendation["fields"]["forAnswer"] == answer["pk"]
        ]

        new_question["answers"].append(
            {
                "answerKey": answer["fields"]["answerKey"],
                "aindex": answer["fields"]["aindex"],
                "uniqueAnswer": answer["fields"]["uniqueAnswer"],
                "score": answer["fields"]["score"],
                "atype": answer["fields"]["atype"],
                "recommendations": related_recommendations,
            }
        )

    new_question["service_category"] = related_category["fields"]["titleKey"]
    new_question["section"] = related_section["fields"]["sectionTitleKey"]

    questions_json.append(new_question)


translations_json = [translation["fields"] for translation in translations]


with open("questions.json", "w") as f:
    f.write(json.dumps(questions_json, indent=2, sort_keys=False))

with open("translations.json", "w") as f:
    f.write(json.dumps(translations_json, indent=2, sort_keys=False))


# print(questions_json)
