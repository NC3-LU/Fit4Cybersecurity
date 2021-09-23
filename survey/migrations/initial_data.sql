/* survey_surveyquestionservicecategory */
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (1, 'SERVCAT001');

/* survey_surveysection */
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (1, 'SECTION001');

/* survey_surveyquestion */
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (1, 'Q001T', 'T', 1, 1, 1, 0);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (2, 'Q002MT', 'MT', 2, 1, 1, 10);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (3, 'Q003ST', 'ST', 3, 1, 1, 15);

/* survey_surveyquestionanswer */
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (1, 'Q001A001', 10, 1, TRUE, 0, 'T');

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (9, 'Q002A001', 10, 2, FALSE, 0, 'P');
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (10, 'Q002A002', 20, 2, TRUE, 10, 'P');
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (11, 'Q002A003', 30, 2, FALSE, 0, 'T');

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (14, 'Q003A001', 10, 3, FALSE, 0, 'P');
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (15, 'Q003A002', 20, 3, FALSE, 5, 'P');
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (16, 'Q003A003', 30, 3, FALSE, 10, 'P');
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score", "atype") VALUES (17, 'Q003A004', 40, 3, FALSE, 0, 'T');


/* survey_recommendations */
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC001', 'a', 'j', NULL, TRUE, 9);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC001', 'a', 'j', NULL, TRUE, 17);


/* survey_translationkey */
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001', ' Service Cat.: Test of free text', 'en', 'C');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001', 'Section: Test of free text', 'en', 'S');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001T', 'Question with free text only (question type "T") ?', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'Please tell about your experience', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002MT', 'Question with multi choice and free text (question type "MT") ?', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'If you would like to have a nice advice, then tick me!', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'Please tick me if like want to get 10 points.', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'Your opinion', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003ST', 'Question with single choice and free text (question type "ST") ?', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'I like Cases...', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'I love Cases :)', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'I passionated to Cases ;)', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'what about you', 'en', 'A');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'The only true wisdom is in knowing you know nothing.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Wonder is the beginning of wisdom.', 'en', 'R');


-- Update the sequences IDs
SELECT setval('survey_surveysection_id_seq', (SELECT MAX(id) from "survey_surveysection"));
SELECT setval('survey_surveyquestionservicecategory_id_seq', (SELECT MAX(id) from "survey_surveyquestionservicecategory"));
SELECT setval('survey_surveyquestion_id_seq', (SELECT MAX(id) from "survey_surveyquestion"));
SELECT setval('survey_surveyquestionanswer_id_seq', (SELECT MAX(id) from "survey_surveyquestionanswer"));
