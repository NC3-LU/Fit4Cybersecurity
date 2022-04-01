import json
import shutil


shutil.copyfile("questions.json", "questions.json.old")
with open("questions.json") as f:
    questions = json.loads(f.read())

shutil.copyfile("translations.json", "translations.json.old")
with open("translations.json") as f:
    translations = json.loads(f.read())


def search(elems, key, lang="en"):
    try:
        return next(
            elem for elem in elems if elem["key"] == key and elem["lang"] == lang
        )["text"]
    except StopIteration:
        return key


for question in questions:
    question["titleKey"] = search(translations, question["titleKey"])
    question["label"] = question.pop("titleKey")

    question["service_category"] = search(translations, question["service_category"])
    question["section"] = search(translations, question["section"])

    for answer in question["answers"]:
        answer["answerKey"] = search(translations, answer["answerKey"])
        answer["label"] = answer.pop("answerKey")

        for recommendation in answer["recommendations"]:
            recommendation["textKey"] = search(translations, recommendation["textKey"])
            recommendation["label"] = recommendation.pop("textKey")

# print(json.dumps(questions, indent=2, sort_keys=False))
with open("questions.json", "w") as f:
    f.write(json.dumps(questions, indent=2, sort_keys=False))


LANGUAGES = ["fr", "de"]  # do not add 'en' in this list
NEW_TRANSLATIONS = []
for translation in [item for item in translations if item["lang"] == "en"]:
    for lang in LANGUAGES:
        NEW_TRANSLATIONS.append(
            {
                "original": translation["text"],
                "translated": search(translations, translation["key"], lang),
                "lang": lang,
            }
        )

# print(json.dumps(NEW_TRANSLATIONS, indent=2, sort_keys=False))
with open("translations.json", "w") as f:
    f.write(json.dumps(NEW_TRANSLATIONS, indent=2, sort_keys=False))
