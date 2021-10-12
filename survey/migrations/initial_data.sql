/* survey_surveyquestionservicecategory */
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (1, 'SERVCAT001PWDS');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (2, 'SERVCAT002SNDA');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (3, 'SERVCAT003WIFI');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (4, 'SERVCAT004RCHA');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (5, 'SERVCAT005TRAI');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (6, 'SERVCAT006BACK');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (7, 'SERVCAT007GDPR');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (8, 'SERVCAT008BYOD');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (9, 'SERVCAT009TELE');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (10, 'SERVCAT010UPDT');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (11, 'SERVCAT011AVIR');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (12, 'SERVCAT012REIT');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (13, 'SERVCAT013CLEA');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (14, 'SERVCAT014PHSE');
INSERT INTO "survey_surveyquestionservicecategory" ("id", "titleKey") VALUES (15, 'SERVCAT015POWR');

/* survey_surveysection */
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (1, 'SECTION001OC');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (2, 'SECTION002GE');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (3, 'SECTION003GT');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (4, 'SECTION004AL');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (5, 'SECTION005RI');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (6, 'SECTION006IT');

/* survey_surveyquestion */
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (1, 'Q001RCHA', 'M', 1, 4, 1, 45);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (2, 'Q002GDPR', 'M', 2, 7, 1, 30);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (3, 'Q003TRAI', 'M', 3, 5, 2, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (4, 'Q004REIT', 'S', 4, 12, 2, 15);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (5, 'Q005TELE', 'M', 5, 9, 2, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (6, 'Q006SNDA', 'M', 6, 2, 3, 15);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (7, 'Q007CLEA', 'M', 7, 13, 3, 30);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (8, 'Q008PWDS', 'M', 8, 1, 4, 45);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (9, 'Q009WIFI', 'M', 9, 3, 5, 25);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (10, 'Q010AVIR', 'M', 10, 11, 5, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (11, 'Q011UPDT', 'M', 11, 10, 6, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (12, 'Q012BACK', 'M', 12, 6, 6, 55);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (13, 'Q013BYOD', 'M', 13, 8, 6, 20);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (14, 'Q014PHSE', 'M', 14, 14, 6, 60);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (15, 'Q015POWR', 'M', 15, 15, 6, 65);


INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (1, 'Q001A001', 10, 1, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (2, 'Q001A002', 20, 1, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (3, 'Q001A003', 30, 1, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (4, 'Q001A004', 40, 1, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (5, 'Q001A005', 50, 1, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (6, 'Q001A006', 60, 1, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (7, 'Q001A007', 70, 1, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (8, 'Q001A008', 80, 1, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (9, 'Q002A001', 10, 2, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (10, 'Q002A002', 20, 2, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (11, 'Q002A003', 30, 2, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (12, 'Q002A004', 40, 2, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (13, 'Q002A005', 50, 2, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (14, 'Q003A001', 10, 3, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (15, 'Q003A002', 20, 3, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (16, 'Q003A003', 30, 3, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (17, 'Q003A004', 40, 3, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (18, 'Q003A005', 50, 3, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (19, 'Q004A001', 10, 4, TRUE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (20, 'Q004A002', 20, 4, TRUE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (21, 'Q004A003', 30, 4, TRUE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (22, 'Q004A004', 40, 4, TRUE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (23, 'Q004A005', 50, 4, TRUE, 0);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (24, 'Q005A001', 10, 5, TRUE, 35);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (25, 'Q005A002', 20, 5, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (26, 'Q005A003', 30, 5, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (27, 'Q005A004', 40, 5, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (28, 'Q005A005', 50, 5, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (29, 'Q005A006', 60, 5, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (30, 'Q006A001', 10, 6, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (31, 'Q006A002', 20, 6, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (32, 'Q006A003', 30, 6, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (33, 'Q006A004', 40, 6, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (34, 'Q007A001', 10, 7, TRUE, 30);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (35, 'Q007A002', 20, 7, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (36, 'Q007A003', 30, 7, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (37, 'Q007A004', 40, 7, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (38, 'Q007A005', 50, 7, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (39, 'Q007A006', 60, 7, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (40, 'Q008A001', 10, 8, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (41, 'Q008A002', 20, 8, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (42, 'Q008A003', 30, 8, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (43, 'Q008A004', 40, 8, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (44, 'Q008A005', 50, 8, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (45, 'Q008A006', 60, 8, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (46, 'Q008A007', 70, 8, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (47, 'Q008A008', 80, 8, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (48, 'Q008A009', 90, 8, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (49, 'Q008A010', 100, 8, FALSE, 10);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (50, 'Q009A001', 10, 9, TRUE, 25);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (51, 'Q009A002', 20, 9, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (52, 'Q009A003', 30, 9, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (53, 'Q009A004', 40, 9, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (54, 'Q009A005', 50, 9, FALSE, 10);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (55, 'Q010A001', 10, 10, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (56, 'Q010A002', 20, 10, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (57, 'Q010A003', 30, 10, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (58, 'Q010A004', 40, 10, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (59, 'Q010A005', 50, 10, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (60, 'Q010A006', 60, 10, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (61, 'Q010A007', 70, 10, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (62, 'Q011A001', 10, 11, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (63, 'Q011A002', 20, 11, FALSE, 15);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (64, 'Q011A003', 30, 11, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (65, 'Q011A004', 40, 11, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (66, 'Q011A005', 50, 11, FALSE, 10);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (67, 'Q012A001', 10, 12, TRUE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (68, 'Q012A002', 20, 12, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (69, 'Q012A003', 30, 12, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (70, 'Q012A004', 40, 12, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (71, 'Q012A005', 50, 12, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (72, 'Q012A006', 60, 12, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (73, 'Q012A007', 70, 12, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (74, 'Q012A008', 80, 12, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (75, 'Q012A009', 90, 12, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (76, 'Q013A001', 10, 13, TRUE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (77, 'Q013A002', 20, 13, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (78, 'Q013A003', 30, 13, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (79, 'Q013A004', 40, 13, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (80, 'Q014A001', 10, 14, FALSE, 0);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (81, 'Q014A002', 20, 14, FALSE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (82, 'Q014A003', 30, 14, FALSE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (83, 'Q014A001', 40, 14, FALSE, 20);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (84, 'Q015A001', 10, 15, FALSE, 25);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (85, 'Q015A002', 20, 15, FALSE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (86, 'Q015A003', 30, 15, FALSE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (87, 'Q015A001', 40, 15, FALSE, 0);

/* survey_recommendations */
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC001', 'a', 'j', NULL, TRUE, 1);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC002', 'a', 'j', NULL, FALSE, 2);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC003', 'a', 'b', NULL, FALSE, 3);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC004', 'c', 'j', NULL, FALSE, 3);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC005', 'a', 'j', NULL, FALSE, 4);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC006', 'a', 'j', NULL, FALSE, 5);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC007', 'a', 'j', NULL, TRUE, 6);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC008', 'a', 'j', NULL, FALSE, 7);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q001REC009', 'a', 'j', NULL, FALSE, 8);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC001', 'a', 'j', NULL, TRUE, 9);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC002', 'a', 'j', NULL, FALSE, 10);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC003', 'a', 'j', NULL, FALSE, 11);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC004', 'a', 'j', NULL, FALSE, 12);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q002REC005', 'a', 'j', NULL, FALSE, 13);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC001', 'a', 'j', NULL, FALSE, 14);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC002', 'a', 'j', NULL, FALSE, 15);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC003', 'a', 'j', NULL, FALSE, 16);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC004', 'a', 'j', NULL, FALSE, 17);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q003REC005', 'a', 'j', NULL, FALSE, 18);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q004REC001', 'a', 'j', NULL, TRUE, 23);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q005REC001', 'a', 'j', NULL, TRUE, 24);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q005REC002', 'a', 'j', NULL, FALSE, 25);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q005REC003', 'a', 'j', NULL, TRUE, 27);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q005REC004', 'a', 'j', NULL, FALSE, 28);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q005REC005', 'a', 'j', NULL, FALSE, 29);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q006REC001', 'a', 'j', NULL, TRUE, 30);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q006REC002', 'a', 'j', NULL, FALSE, 31);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q006REC003', 'a', 'j', NULL, FALSE, 32);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q006REC004', 'a', 'j', NULL, FALSE, 33);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC001', 'a', 'j', NULL, TRUE, 34);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC002', 'a', 'j', NULL, FALSE, 35);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC003', 'a', 'j', NULL, FALSE, 36);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC004', 'a', 'j', NULL, FALSE, 37);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC005', 'a', 'j', NULL, FALSE, 38);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q007REC006', 'a', 'j', NULL, FALSE, 39);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC001', 'a', 'j', NULL, TRUE, 40);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC002', 'a', 'j', NULL, TRUE, 41);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC003', 'a', 'j', NULL, TRUE, 42);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC004', 'a', 'j', NULL, FALSE, 43);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC005', 'a', 'j', NULL, FALSE, 44);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC006', 'a', 'j', NULL, FALSE, 45);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC007', 'a', 'j', NULL, FALSE, 46);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC008', 'a', 'j', NULL, FALSE, 47);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC009', 'a', 'j', NULL, TRUE, 48);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q008REC010', 'a', 'j', NULL, FALSE, 49);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q009REC001', 'a', 'j', NULL, TRUE, 50);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q009REC002', 'a', 'j', NULL, TRUE, 51);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q009REC003', 'a', 'j', NULL, TRUE, 52);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q009REC004', 'a', 'j', NULL, FALSE, 53);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q009REC005', 'a', 'j', NULL, FALSE, 54);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC001', 'a', 'j', NULL, TRUE, 55);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC002', 'a', 'j', NULL, FALSE, 56);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC003', 'a', 'j', NULL, FALSE, 57);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC004', 'a', 'j', NULL, FALSE, 58);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC005', 'a', 'j', NULL, FALSE, 59);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC006', 'a', 'j', NULL, FALSE, 60);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q010REC007', 'a', 'j', NULL, FALSE, 61);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q011REC001', 'a', 'j', NULL, TRUE, 62);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q011REC002', 'a', 'j', NULL, FALSE, 63);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q011REC003', 'a', 'j', NULL, FALSE, 64);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q011REC004', 'a', 'j', NULL, FALSE, 65);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q011REC005', 'a', 'j', NULL, FALSE, 66);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC001', 'a', 'j', NULL, TRUE, 67);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC002', 'a', 'j', NULL, FALSE, 69);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC003', 'a', 'j', NULL, FALSE, 70);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC004', 'a', 'j', NULL, FALSE, 71);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC005', 'a', 'j', NULL, FALSE, 72);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC006', 'a', 'j', NULL, FALSE, 73);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC007', 'a', 'j', NULL, FALSE, 74);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q012REC008', 'a', 'j', NULL, FALSE, 75);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q013REC001', 'a', 'j', NULL, TRUE, 76);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q013REC002', 'a', 'j', NULL, FALSE, 77);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q013REC003', 'a', 'j', NULL, FALSE, 78);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q013REC004', 'a', 'j', NULL, FALSE, 79);



INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q014REC001', 'a', 'j', NULL, FALSE, 80);
/*INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q014REC002', 'a', 'j', NULL, FALSE, 81);*/
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q014REC003', 'a', 'j', NULL, FALSE, 82);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q014REC004', 'a', 'j', NULL, FALSE, 83);

INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q015EC001', 'a', 'j', NULL, FALSE, 84);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q015REC002', 'a', 'j', NULL, FALSE, 85);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q015REC003', 'a', 'j', NULL, FALSE, 86);
INSERT INTO "survey_recommendations" ("textKey", "min_e_count", "max_e_count", "sector", "answerChosen", "forAnswer_id") VALUES ('Q015REC004', 'a', 'j', NULL, FALSE, 87);


/* survey_translationkey */
-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Mots de passe', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Contrats (SLA/NDA)', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'Wifi', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Règles/Chartes', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Formations', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Sauvegardes', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'GDPR', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Télétravail/Mobilité', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'Postes Utilisateurs/Mises à jour', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Antivirus', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'Responsabilités IT et Sécurité de l''Information', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Nettoyage des Locaux', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT014PHSE', 'Sécurité physique', 'fr', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT015POWR', 'Alimentation de secours', 'fr', 'C');
-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Passwords', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Contracts (SLA/NDA)', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'WiFi', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Rules/Charter', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Trainings', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Backups', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'GDPR', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Home Office/Mobility', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'User Work Stations/Updates', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Anti-virus', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'IT and Information Security Responsibilities', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Office Cleaning', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT014PHSE', 'Physical Security', 'en', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT015POWR', 'Backup Power Supply', 'en', 'C');

-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Passwörter', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Verträge (SLA/NDA)', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'WLAN', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Regeln/Charter', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Schulungen', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Backup', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'DSGVO', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Heimarbeit/Mobilität', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'Benutzerarbeitsplätze/Updates', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Antivirus', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'Verantwortlichkeiten für Anti-VirusIT und Informationssicherheit', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Büroreinigung', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT014PHSE', 'Physische Sicherheit', 'de', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT015POWR', 'Notstromversorgung', 'de', 'C');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Obligations et Conformités', 'fr', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Gestion des Employés', 'fr', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Gestion des Tiers', 'fr', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Accès Logiques', 'fr', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Réseau Interne', 'fr', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Infrastructure IT', 'fr', 'S');
-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Awareness and Compliance', 'en', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Employee Management', 'en', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Third Party Management', 'en', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Logical Access', 'en', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Local Area Network', 'en', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Information System', 'en', 'S');
-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Bewusstsein und Konformität', 'de', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Verwaltung von Mitarbeiter', 'de', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Verwaltung von Dritte', 'de', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Logischer Zugriff', 'de', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Lokales Netzwerk', 'de', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Informationssystem', 'de', 'S');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'Dans l''entreprise, les règles données aux employés sont', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'non décrites', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'transmises oralement à toutes et tous', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'écrites et données par mail', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'lues et signées par tous, et inscrites dans une charte', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'écrites/expliquées avec du vocabulaire simple, non spécifique à un métier', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'assez longues, mais très précises', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'données avec des conseils et des bonnes pratiques pour faciliter la vie des employés', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'adaptées selon la personne la personne et/ou son rôle', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'Dans l''entreprise, sont défini', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'aucune autre donnée personnelle que celles des employés, ou aucune gestion concernant les données personnelles', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'une personne responsable de toutes les actions liées aux données personnelles', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'une explication écrite sur le cycle de vie des données internes (comment elles sont récupérées, comment elles sont stockées, où et quand elles sont détruites...)', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'une explication orale ou écrite pour les employés sur le comportement à adopter pour les cas concernant les données personnelles', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'une vidéosurveillance ou une prise d''image comme donnée personnelle, particulièrement si elle contient une personne ou une identité avec un lieu', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Les employés sont formés', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'à leur métier par leurs études ou cursus scolaire, mais aussi avec des formations supplémentaires pour mettre à jour les connaissances', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'aux logiciels qu''ils utilisent quotidiennement', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'à la sécurité de l''information pour avoir les clés en main afin de se défendre contre d''éventuelles attaques', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'en interne ou en externe par des spécialistes', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'et sensibilisés à l''importance de conserver confidentiellement les données, particulièrement si elles sont personnelles', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'Les responsabilités IT et Sécurité de l''Information', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'sont définis en interne, avec une personne spécialisée à régler les problèmes informatiques', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'sont définis en interne, avec deux personnes aux formations et métiers spécialisés dans le domaine', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'sont définis en externe, par un contrat', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'sont définis en externe, sur demande selon les besoins, sans contrat pour lier les entreprises', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'ne sont pas définis; chacun résout son problème ou fait appel à un autre employé avec plus de compétence dans le domaine', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'Les employés, lors d''un voyage à l''extérieur, utilisent', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'aucun appareil professionnel, car le télétravail n''est pas une pratique autorisée et la seule connexion possible au réseau d''entreprise est interne', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'un VPN (Virtual Private Network) est utilisé pour chiffrer les données lors de toute connexion sur le serveur interne de l''entreprise', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'un WiFi public, une connexion ouverte, ou une connexion protégée par mot de passe d''un organisme ou d''une personne externe', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'une connexion privée ou du partage de réseau d''un téléphone personnel ou professionnel', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'un filtre à écran, ou portent une attention particulière à la vision possible sur les écrans au travers des fenêtres ou dans les transports publics', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'un matériel avec un stockage de données chiffré ou sans données confidentielles pour éviter toute perte involontaire de données', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Des contrats avec les différents prestataires (informatique, comptabilité...)', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'ne sont pas définis, et ces derniers n''interviennent uniquement en cas de besoin de façon ponctuelle', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'définissent la confidentialité des données et la protection nécessaire de ces dernières', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'définissent le temps maximum pour lequel ces derniers doivent intervenir', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'sont régulièrement revus pour s''assurer qu''ils correspondent toujours aux besoins', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'Le nettoyage des locaux de travail se déroule', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'en interne, par les employés, de façon ponctuelle', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'pendant les heures de bureau', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'sous couvert de règles données concernant ce qu''il faut éviter de faire, ou éviter de toucher', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'sous couvert d''un contrat spécifiant la confidentialité à respecter', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'alors que tous documents confidentiels sont verrouillés à clé, dans des armoires, des bureaux, ou une salle spécifique', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'en évitant les salles ou les accès sont interdits, comme une salle d''archive ou une salle serveur', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Les mots de passe dans l''entreprise', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'ne sont pas soumis à des consignes ou conseils particuliers, ou sont laissés à discrétion de chacun', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'sont centralisés dans un fichier, ou tous connus par une ou plusieurs personnes', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'sont partagés selon le besoin d''accéder à une machine', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'font 12 caractères ou plus, et possèdent au moins une majuscule, une minuscule, un chiffre et un caractère spécial', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'ne forment pas des mots ou des dates cohérentes', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'sont des phrases complètes', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'sont changés régulièrement, tous les ans ou tous les deux ans', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'sont inclus dans un gestionnaire de mots de passe', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'sont sauvegardés dans les navigateurs Web', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'sont différents pour chaque application, même pour un utilisateur', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Les réseaux sans fil', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'ne sont pas activés dans l''organisme', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'sont utilisés sans distinctions par des externes comme des personnes internes à l''entreprise', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'sont donnés sans distinctions à des externes comme des personnes internes à l''organisme et sans récolte d''identité', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'sont protégés par des mots de passe très longs (plus de 20 caractères) différents de celui par défaut', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'des imprimantes sont protégées par un mot de passe', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Un logiciel antivirus', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'n''est pas installé ou utilisé', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'est installé sur toutes les machines de bureau et les ordinateurs portables', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'est mis à jour sur toutes les machines, de façon automatique comme manuelle', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'est activé et protège les machines de façon proactive', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'est installé sur tous les téléphones mobiles étant sur le réseau', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'est utilisé de temps à autre pour analyser la bonne santé d''une machine, même sans évènements externes', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'est utilisé pour analyser le réseau en cas de suspicion d''infection', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'Les postes utilisateurs sont', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'laissés sans consignes à discrétion des utilisateurs', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'mis à jour de façon automatique ou manuelle (logiciels comme système d''exploitation)', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'soumis aux droits d''administration, qui empêche pour tout utilisateur d''installer un logiciel', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'soumis à des règles et des consignes en ce qui concerne l''installation et le téléchargement de programme, comme sur l''illégalité, ou éviter d''installer sans faire attention', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'verrouillés en cas d''une brève absence, même pour en temps très court', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Les sauvegardes sont', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'inexistantes: elles ne sont pas faites ou non fonctionnelles', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'transférées: le prestataire informatique en a la responsabilité à travers le Cloud', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'exhaustives: toutes les données qui doivent être incluses dans les sauvegardes, et tous les utilisateurs en sont conscients et ne stockent pas de données en local', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'journalières: les sauvegardes sont faites tous les jours ou plus', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'retenues: il est possible de remonter dans le temps dans les sauvegardes à 1 mois ou plus ', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'délocalisées: le serveur et les sauvegardes ne sont pas au même endroit, à plus de 3 kilomètres de distance', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'déconnectées: au moins en partie débranchées du serveur une fois qu''elles ont été faites', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'testées: un ou plusieurs fichiers sont restaurés à partir d''une sauvegarde de temps en temps', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'chiffrées: si elles sont amenées en dehors de l''entreprise, elles doivent être illisibles', 'fr', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'La pratique d''amener du matériel personnel informatique (Clé USB, disque dur, mobile, tablette, laptop ...) dans l''environnement professionnel (réseau qui se connecte au serveur)', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'est interdite ou impossible dans l''organisme', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'est soumise à des règles précises, particulièrement en cas d''insertion sur le réseau interne de l''organisme', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'est soumise à un contrôle strict', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'a été expliquée aux employés à travers des formations ou des explications', 'fr', 'A');


INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014PHSE', 'Pendant une panne de courant', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A001', 'une alimentation électrique de secours n''existe pas pour assurer la continuité des activités', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A002', 'l''entreprise dispose d''un générateur utilisé comme alimentation de secours', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A003', 'l''entreprise dispose d''un système d''énergie renouvelable comme alimentation de secours', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A004', 'les systèmes et serveurs critiques sont connectés à un onduleur', 'fr', 'A');


INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015POWR', 'L''accès au bâtiment et bureau de l''entreprise est assuré', 'fr', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A001', 'par un système d''accès électronique par badge, basé sur le profil de la personne', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A002', 'par un système d''accès électronique par badge, basé sur le profil de la personne', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A003', 'un system de vidéo-surveillance', 'fr', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A004', 'par aucune mesure de sécurité physique', 'fr', 'A');


-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'In the company, rules are', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'not described', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'orally given', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'written and given by mail', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'read and signed by everyone, in a user charter', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'written and explained with simple words, which are non-specific to a type of work', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'quite heavy, but really accurate', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'given with advice and the best practices', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'adapted depending on the role of the reader', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'In the company, there is/are', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'no personal data other than the employee data, or nothing related to the personal data', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'someone who does every action bound to personal data', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'a written explanation about the personal data lifecycle (how there are get, stored, and when and how they are destroyed)', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'an oral or a written explanation of what should be done when there is a problem with personal data', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'some video surveillance, or some pictures taken, that contains face or people and possibly location data', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Employees are trained for/in', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'their work, their daily tasks by their studies, but also receive trainings to update their knowledge', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'the software they daily use', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'information security, to have the knowledge to protect themselves against attacks', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'by specialists, that could be internal or external', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'the importance to keep confidential data confidential, and more importantly if they are personal', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'IT and Information Security responsibilities are:', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'internally defined, with someone who is specialised in IT field', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'internally defined, with at least two people that were trained in the field', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'externally defined, with a contract', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'externally defined, depending on the needs, without any contract specified', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'aren''t defined; anyone tries to resolve their problems, asking someone else if they can', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'During any trip outside the company, the employee uses', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'no professional tools because home office or travel is not allowed or necessary, or the only connection to the internal network is on the company premises', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'VPN (Virtual Private Network) is used to encrypt all data from any external network to the internal server', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'public Wi-Fi, open networks or connection protected by external organisation or person', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'a private connection or a connection sharing from a private or professional smartphone (tethering/hotspot)', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'a screen filter or adjusts their position to ensure that no unauthorised person could see what is on the screen', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'devices that are encrypted (protected by a password at boot) or without any confidential data', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Contracts with third parties', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'are not defined, because they only come punctually in case of an incident or needs', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'define confidentiality of data, and their protection', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'define the maximum time of intervention after an incident', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'are regularly reviewed to ensure that they correspond to the needs', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'The office cleaning is done', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'internally, by employees, punctually', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'during the work time', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'with rules of what should be done and what should not be done', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'with a contract which specifies confidentiality', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'with all confidential documents locked in a room, a desk or a closet', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'while avoiding rooms which have restricted access, like an archive room or a server room', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Passwords in the company are', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'not having requirements or guidelines, employees are left on their own', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'centralised in a file, or are all known by one or more people', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'shared whenever there is a need to access a protected device', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'made up of 12 or more characters which are uppercase, lowercase, digits and special character', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'not forming any words or dates', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'complete sentences', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'regularly changed, every year or two', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'included in a password manager', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'included in web browsers', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'different for each application used, even for a user', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Wireless networks', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'are not used in the company', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'are used by everyone and access is granted to the company server', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'are given to everyone, without any way to get identity of the persons', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'are protected by long passwords of 20 characters or more', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'of the printers are protected by a strong password', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Antivirus software', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'is not installed or used', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'is installed on computers and laptops', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'is updated on all computers, automatically or manually', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'is activated and protects computers', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'is installed on all mobile phones that are on networks', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'is used from time to time in order to analyse the computer, even without external events', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'is used to analyse the network whenever a suspicious event occurs', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'The user workstations are', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'left without any rules, and users have to take care of their on workstations', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'automatically or manually updated; software and operating system', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'controlled by administrators, which won''t let users install software because they do not have administrator rights', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'needed to comply with rules or guidelines about installation and downloading software, concerning illegality or the danger to install something without authorisation', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'locked whenever the user is not at his desk, even for a short time', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Backups are', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'non existent: they are not done or not working', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'shared: a third party has the responsibility of the backup', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'exhaustive: all data is on backups, and all users know that and avoid storing information locally', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'done daily: backups are made at least once daily', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'retained: it is possible to get back a month or more', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'decentralized: the server, and at least one full backup system is separated by at leaset 3 kilometres', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'disconnected: they are disconnected from the server once they are done', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'tested: one or all the files are restored from a backup from occasionally', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'encrypted: so when they are taken outside the company, they can''t be read', 'en', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'Having some personal IT devices (USB Key, Hard Drive, Smartphone, Tablet, Laptop ...) in the professional environment (network that is connected to the server)', 'en', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'is forbidden or impossible in the company', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'is subject to precise rules, particularly before connecting to the company network', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'is under a strict anti-virus control', 'en', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'has been explained to employees through training or explanations', 'en', 'A');



    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014PHSE', 'During a power outage', 'en', 'Q');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A001', 'backup power supply does not exist to inssure business continuity', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A002', 'the company dispose of a generator that is used as backup power supply', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A003', 'the company dispose of renewable energy system as a backup power supply', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A004', 'critical systemys and servers are connected to an UPS', 'en', 'A');


    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015POWR', 'The access to the building and office of the company is ensured', 'en', 'Q');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A001', 'by an electronic access system, based on the person''s profile', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A002', 'by a security guard who controls the exits and entrances to the building', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A003', 'a video surveillance system', 'en', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A004', 'no physical security measures exist', 'en', 'A');


-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'In der Firma werden Regeln', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'nicht beschrieben', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'mündlich übertragen', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'geschrieben und per Mail mitgeteilt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'von allen gelesen und unterschrieben und in einer Benutzercharta festgehalten', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'geschrieben und erklärt mit einfachen Worten, die unabhängig des Arbeitsbereiches sind', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'ziemlich schwer, aber sehr genau', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'mit Rat und den besten Praktiken übermittelt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'angepasst je nach Rolle des Lesers', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'In der Firma gibt es / sind', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'keine personenbezogenen Daten als die der Angestellten oder keine personenbezogenen Daten', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'jemand, der jede an persönliche Daten gebundene Handlung ausführt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'eine schriftliche Erklärung über den Lebenszyklus personenbezogener Daten (wie sie abgerufen, gespeichert und wann und wie sie vernichtet werden)', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'eine mündliche oder schriftliche Erklärung, was zu tun ist, wenn es ein Problem mit personenbezogenen Daten gibt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'einige Videoüberwachungen oder einige aufgenommene Bilder, die Gesichter oder Personen enthalten, die allen erklärt werden', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Die Mitarbeiter sind ', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'geschult um ihre Arbeit, ihre täglichen Aufgaben zu bewältigen; durch ihr Studium, aber auch durch regelmäßge Fortbildung', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'geschult um die Software, die sie täglich brauchen benutzen zu können', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'geschult in Informationssicherheit, um sich vor Angriffen schützen zu können', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'von internen oder externen Spezialisten geschult.', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'geschult die Wichtigkeit zu erkennen, einige Daten vertraulich zu behandeln, persönliche Daten inklusive', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'IT- und Informationssicherheitsaufgaben sind:', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'intern definiert, mit jemandem, der im IT-Bereich spezialisiert ist', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'intern definiert, mit mindestens zwei Personen, die auf dem Feld geschult wurden', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'extern definiert, mit einem Vertrag', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'extern definiert, je nach Bedarf, ohne Angabe eines Vertrages', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'sind nicht definiert; Jeder versucht, seine Probleme selbst zu lösen oder fragt jemanden der es kann', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'Während einer Mission außerhalb des Unternehmens verwendet der Mitarbeiter', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'keine professionellen Werkzeuge, da Home Office oder Reisen nicht zulässig oder erforderlich sind oder die einzige Verbindung zum internen Netzwerk auf dem Firmengelände besteht', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'VPN (Virtuelles privates Netzwerk) wird verwendet, um alle Daten von einem beliebigen Netzwerk zum internen Server zu verschlüsseln', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'öffentliches WLAN, offene Netzwerke oder Verbindungen, die durch eine externe Organisation oder Person geschützt sind', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'eine private Verbindung oder eine gemeinsame Nutzung von Verbindungen von einem privaten oder professionellen Smartphone', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'einen Bildschirmfilter oder deren Aufmerksamkeit, um sicherzustellen, dass keine nicht autorisierte Person sehen kann, was sich auf dem Bildschirm befindet', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'Geräte, die verschlüsselt (durch ein Passwort beim Booten geschützt) oder ohne vertrauliche Daten sind', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Verträge, die mit Dritten geschlossen werden', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'sind nicht definiert, weil Dritte nur im Falle eines Ereignisses oder Bedarfs gerufen werden', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'definieren Vertraulichkeit von Daten und deren Schutz', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'definieren die maximale Eingriffszeit nach einem Vorfall', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'werden regelmäßig überprüft, um sicherzustellen, dass sie den Bedürfnissen entsprechen', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'Die Büroreinigung wird', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'intern, von Mitarbeitern, pünktlich  erledigt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'während der Arbeitszeit erledigt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'nach defininierten Anweisungen erledigt (was getan werden soll und was nicht)', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'gemäß einem Vertrag erledigt, der auch zu Vertraulichkeit/Geheimhaltung zwingt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'durchgeführt, während alle vertraulichen Dokumente in einem Raum, einem Schreibtisch oder einem Schrank eingeschlossen', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'erledigt und Räume, die als beschränkt zugänglich eingestuft sind, wie ein Archivraum oder ein Serverraum, werden vermieden', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Passwörter in der Firma sind', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'keine Ratschlägen oder Richtlinien gegeben, oder muss selber entscheiden', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'zentralisiert in einer Datei oder alle, die einer oder mehreren Personen bekannt sind', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'freigegeben, wenn auf ein geschütztes Gerät zugegriffen werden muss', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'aus 12 oder mehr Buchstaben bestehend aus Groß- und Kleinbuchstaben, Ziffern und Sonderzeichen', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'keine Wörter oder Daten (wie Geburtsdatum etc.)', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'vollständige Sätze', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'regelmäßig zu wechseln; z.B. jedes Jahr oder alle zwei Jahre', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'in einem Passwort-Manager abgelegt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'in Webbrowsern abgelegt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'für jede verwendete Anwendung unterschiedlich, auch für den Benutzer', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Drahtlose Netzwerke', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'werden im Unternehmen nicht verwendet', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'werden von allen genutzt und der Zugriff auf den Unternehmensserver ist gewährt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'werden jedem gegeben, ohne die Identität der Personen zu bekommen', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'sind durch lange Passwörter mit mindestens 20 Zeichen geschützt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'der Drucker sind durch ein starkes Passwort geschützt', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Antiviren Software', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'ist nicht installiert oder wird nicht verwendet', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'ist auf Computern und Laptops installiert', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'wird auf allen Computern automatisch oder manuell aktualisiert', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'ist aktiviert und schützt den Computer', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'ist auf allen Mobiltelefonen in Netzwerken installiert', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'wird von Zeit zu Zeit verwendet, um den Computer auch ohne externe Ereignisse zu analysieren', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'wird verwendet, um das Netzwerk zu analysieren, wenn ein verdächtiges Ereignis auftritt', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'Die Computer der Benutzer', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'haben keine Regeln für die Benutzung, und Benutzer müssen sich selbst um ihren Computer kümmern', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'werden automatisch oder manuell aktualisiert, Software als Betriebssystem', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'werden von Administratoren gewarted, somit können Benutzer keine Software installieren', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'werden nur mit einhalten der Regeln genutzt, die über die Installation und das Herunterladen von Software, die Rechtswidrigkeit oder die Gefahr der unbefugten Installation informieren', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'sind gesperrt, wenn der Benutzer nicht an seinem Rechner ist; auch wenn die Abwesenheit nur für kurze Zeit ist', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Backups (Datensicherunged) sind', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'nicht existent: sie sind nicht gemacht oder funktionieren nicht', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'geteilt: ein Dritter hat die Verantwortung für die Sicherung', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'vollständig: Alle Daten befinden sich in Backups und alle Benutzer ist bekannt Daten daher nicht lokal zu speichern', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'täglich erledigt: Backups werden jeden Tag oder öfter erstellt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'länger gespeichert: Es sollte möglich sein, mindestens einen Monat vorher zurückzukehren', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'dezentralisiert: Die Server, welche ein vollständiges Backup speichern sind mindestens 3 Kilometer voneinander entfernt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'entstöpselt: Sie werden vom Server getrennt, sobald sie fertig sind', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'geprüft: Von Zeit zu Zeit werden einige oder alle Dateien aus einem Backup wieder hergestellt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'verschlüsselt: Wenn sie aus dem Unternehmen gebracht werden, können sie nicht gelesen werden', 'de', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'Das Mitbringen persönliche IT-Geräte (USB-Stick, Festplatte, Smartphone, Tablet, Laptop ...) im professionellen Umfeld (Netzwerk, das mit dem Server verbunden ist)', 'de', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'ist in der Firma verboten oder unmöglich', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'ist nur unter Einhaltung strenger Regeln, speziell wenn sie mit dem internen Netzwerk verbunden werden, genemigt', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'unterliegen strenger kontrollen', 'de', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'wurde den Mitarbeitern durch Schulungen oder Erklärungen erklärt und gegebenefalls untersagt', 'de', 'A');


    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014PHSE', 'Während eines Stromausfalls', 'de', 'Q');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A001', 'es gibt keine Notstromversorgung, um die Geschäftskontinuität zu gewährleisten', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A002', 'das Unternehmen verfügt über einen Generator, der als Notstromversorgung genutzt wird', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A003', 'das Unternehmen verfügt über ein System zur Nutzung erneuerbarer Energien als Notstromversorgung', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014A004', 'kritische Systeme und Server sind an eine USV angeschlossen', 'de', 'A');


    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015POWR', 'Der Zugang zum Firmengebäude und zum Büro ist gewährleistet', 'de', 'Q');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A001', 'durch ein elektronisches Zugangssystem, das auf dem Profil der Person basiert', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A002', 'durch einen Wachmann, der die Ausgänge und Eingänge des Gebäudes kontrolliert', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A003', 'ein Videoüberwachungssystem', 'de', 'A');
        INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015A004', 'keine physischen Sicherheitsmaßnahmen', 'de', 'A');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'L''entreprise doit définir des règles pour éviter toutes incompréhensions.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Les règles (qu''elles soient organisationnelles, métier, ou à l''usage de l''informatique) doivent être connues et expliquées à tous, au moins oralement au possible.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'Si une transmission orale suffit dans un cadre "familial", les règles devraient être mises dans une charte ou un règlement, écrites et signées par tous, particulièrement en cas de croissance.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'Une transmission uniquement orale peut rapidement devenir compliquée quand il y a beaucoup de personnes, et devient vite ingérable lors des phases de départ et d''arrivée du personnel importante.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Les règles écrites et signées ont l''avantage :
	- d''éviter les oublis.
	- d''avoir une preuve juridique que les règles sont connues.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'Dans la mesure du possible, ses dernières doivent être simples et courtes surtout pour être attractive et lisible.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Des règles trop longues ou trop lourdes de vocabulaire technique pourront devenir confuses pour les employés.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Si possible, il ne faut pas hésiter à donner des astuces pour aider au respect des règles, voire parfois, expliquer en quoi elles sont nécessaires.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Aussi, des petites adaptations doivent être pensées selon le rôle, ou si le contrat est temporaire par exemple.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'Pour le moment l''entreprise ne dispose que peu de données personnelles. Cependant, particulièrement si le nombre de traitements auguemente, ou si rien de particulier n''a été fait, il faut penser:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Définir, dans la mesure du possible, une personne qui est responsable de la gestion des données pour éviter le manque de réponse en cas d''incident.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Le cycle de vie des données personnelles doit être accessible pour n''importe qui (registre de traitement) ;
	- Comment sont-elles obtenues ?
	- Comment sont-elles traitées ?
	- Comment sont-elles accessibles et par qui, sous quelles clauses ?
	- Comment sont-elles modifiables ?
	- Combien de temps sont-elles conservées ?
	- Comment sont-elles détruites ?
Ce cycle devrait être décrit quelque part et accessible à tous (contrat de vente, site web, fichier présentable en cas d''interrogation ...).', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'Dans l''idéal, les employés, principalement au contact des clients, doivent connaître la personne responsable pour renvoyer correctement la requête, mais aussi la sensibilité des données manipulées.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'Une autorisation doit être demandée pour le droit à l''image (droit de prendre le cliché comme sa diffusion), et les personnes doivent être conscientes d''une vidéosurveillance.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Les formations métier sont importantes et doivent être mises régulièrement à jour pour s''assurer d''avoir les dernières pratiques et éviter les pertes de temps inutiles.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Des formations sur les logiciels utilisés de façon quotidienne évitent principalement les mauvaises gestions et les erreurs de manipulations.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'S''informer sur les différents types d''attaques existants et les moyens pouvant mis être en œuvre pour une attaque permet au possible d''éviter des comportements menant à la réussite de ces dernières.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Des formations faites en interne n''ont parfois pas le même impact que celles faites en externe, mais sont tout aussi valables, et parfois même plus appropriées pour la maîtrise du sujet et de la bonne orientation du discours.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Sensibiliser les utilisateurs à la sensibilité des informations manipulés pour attirer leur attention sur les protections à mettre en œuvre.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'Il est important de définir les responsabilités, que ce soit en interne ou en externe, avec une ou plusieurs personnes, ou une entreprise vraiment spécialisée dans le domaine de la responsabilité, avec au possible une formation.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'Pour le moment, aucun travail à l''extérieur n''est fait. Si cela est néanmoins amené à changer à jour, il est important de faire attention :
	- Les connexions extérieures non contrôlées doivent être évitées pour éviter d''éventuelles pertes de données.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Quand une connexion est faite de l''extérieur vers l''entreprise, il est important d''accéder au réseau interne par l''intermédiaire d''un VPN pour s''assurer que les données restent confidentielles.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'Les connexions extérieures non contrôlées doivent être évitées pour éviter d''éventuelles pertes de données.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'Une attention particulière doit être apportée à l''environnement visuel pour éviter les regards indiscrets ou de l''éventuel espionnage.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Le matériel doit être chiffré s''il contient des données confidentielles pour éviter toute perte de confidentialité.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'Pour le moment, aucun contrat avec les prestataires n''est signé. Si cela est néanmoins amené a changer à jour, il est important de faire attention:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'Si des données confidentielles sont accessibles par différents prestataires, par exemple des données financières par une fiduciaire, ou des données sur un serveur accessible à un prestataire informatique, il est nécessaire de les protéger avec un contrat de confidentialité.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'Si les moyens et le contexte le permettent et le nécessitent, un contrat est nécessaire pour assurer la disponibilité, tant les informations nécessaires, que le matériel pour les manipuler.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'Il faut régulièrement revoir les contrats assurant une certaine disponibilité pour s''assurer:
	- de ne pas se retrouver sans intervention dans un délai où cette dernière serait indispensable;
	- de ne pas surpayer un prestataire pour un temps d''intervention trop élevé;
	- que les services rendus sont d''un niveau de qualité suffisant à ce qui est nécessaire.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'Pour le moment, aucun prestataire ne réalise le nettoyage des locaux. Si cela est néanmoins amené a changer à jour, il est important de faire attention:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'Le nettoyage des locaux doit se faire, dans la mesure du possible, pendant les heures de bureau pour éviter des éventuels vols de données.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Des règles doivent être données pour principalement spécifier ce qu''il faut faire où éviter de toucher.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'Il faut également un contrat de confidentialité, car il est souvent possible d''entendre ou de remarquer des données confidentielles, même si l''accès n''est pas spécifiquement officiel.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'Pour éviter les problèmes de curiosité humaine, les documents confidentiels doivent être inaccessibles, surtout à première vue.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'Le personnel d''entretien ne doit pas intervenir dans un local à accès restreint, comme une salle d''archive ou une salle serveur.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Il est nécessaire de donner des consignes pour éviter les mots de passe faibles. Des astuces et techniques peuvent être données pour éviter l''oubli fréquent de ces derniers. En voici quelques exemples :
	- Les mots de passe doivent être personnels, et personne d''autre ne doit en avoir la connaissance. En cas de besoin, chacun doit pouvoir accéder aux fichiers à partir de son mot de passe personnel.
	- Il faut éviter d''avoir une machine accessible par un seul et unique accès, et partagée. Si c''est inévitable, alors il est nécessaire de définir un responsable de cette machine, chargé d''en assurer sa bonne utilisation, et de donner les accès les plus limités possible.
	- Les navigateurs internet ne stockent pas les mots de passe de façon protégés, et cette fonctionnalité est donc à éviter.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Ces derniers doivent également être personnels, et personne d''autre ne doit en avoir la connaissance. En cas de besoin, chacun doit pouvoir accéder aux fichiers à partir de son mot de passe personnel.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Il faut éviter d''avoir une machine accessible par un seul et unique accès. Si c''est inévitable, alors il est nécessaire de définir un responsable de cette machine, chargé d''en assurer sa bonne utilisation, et de donner les accès les plus limités possible.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'Il est nécessaire d''avoir des mots de passe ayant au moins une majuscule, une minuscule, un chiffre et un caractère spécial, pour un total de 12 caractères ou plus.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Les mots de passe ne doivent pas former des mots ou des dates cohérentes pour qu''ils ne soient pas facilement devinables.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Des phrases complètes peuvent être utilisées comme mot de passe, même s''ils forment des mots complets.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Les mots de passe doivent être changés de temps à autre pour prévenir une possible fuite de ses dernières.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'Des gestionnaires de mot de passe peuvent être utilisés pour faciliter la gestion et leur stockage.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'Les navigateurs internet ne stockent pas les mots de passe de façon protégés, et cette fonctionnalité est donc à éviter.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Les mots de passe réutilisés dans d''autres sites offrent plus de chance de divulgation. De plus, une seule perte de mot de passe suffit à compromettre la totalité des accès.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'Pour le moment, les réseaux sans fil ne sont pas activés dans l''entreprise. Si cela est néanmoins amené à changer à jour, il est important de faire attention:
	- Dans l''idéal, les réseaux sans fil doivent être séparés entre les utilisateurs externes et internes pour éviter de nombreux problèmes d''accès.
	- Si un réseau sans fil pour des personnes externes, des protections lourdes doivent être mises en place, comme une récolte d''identité pour désigner le responsable d''une connexion à du contenu qui outrepasserait le cadre légal.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Dans l''idéal, les réseaux sans fil doivent être séparés entre les utilisateurs externes et internes pour éviter de nombreux problèmes d''accès.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'Si un réseau sans fil pour des personnes externes, des protections lourdes doivent être mises en place, comme une récolte d''identité pour désigner le responsable d''une connexion à du contenu qui outrepasserait le cadre légal.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'Le mot de passe du réseau sans fil ne doit pas être facilement devinable pour éviter des connexions non désirées.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Les réseaux WiFi d''imprimante, s''ils sont nécessaires, doivent être protégés pour éviter toute fuite des documents imprimés et scannés.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'L''entreprise doit se munir d''antivirus, et faire attention:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'Un logiciel antivirus doit être installé sur les machines pour empêcher au maximum possible les infections virales.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'Ce dernier doit être mis à jour, au moins de façon automatique pour couvrir le plus de menaces possible.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'Il doit être également activé en permanence pour protéger en continu la machine.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'Tout appareil, y compris des appareils plus nomades comme les ordinateurs portables, les téléphones et les tablettes doivent avoir un antivirus, même ceux proposés par défaut dans les systèmes d''exploitation.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Dans l''idéal, il ne faut pas hésiter à faire des tests de temps à autre.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Des tests doivent être réalisés dès lors d''une suspicion d''infection.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Des consignes et un encadrement précis doivent être donnés aux utilisateurs de station de travail. Voici des points à donner:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'Une machine doit être le plus à jour possible pour éviter le plus de failles, et ainsi éviter au possible les attaques par intrusion dans le réseau. Si beaucoup de systèmes d''exploitation se mettent à jour sans aide particulière, les logiciels doivent recevoir une attention particulière.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Les droits d''administration peuvent être laissés à des utilisateurs avertis et informés des consignes pour utiliser leur machine, mais nécessitent des règles précises.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Les téléchargements doivent être sur les sites officiels, tant pour éviter d''éventuels téléchargements illégaux que les différents virus, et ces consignes doivent être données.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Les machines doivent être verrouillées pour éviter toute usurpation d''identité.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'Il est important d''avoir des sauvegardes pour de nombreuses raisons, comme s''assurer d''avoir une redondance des données. Il est important d''avoir et de respecter:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Les sauvegardes doivent concerner toutes les données de l''entreprise, et il est important d''en faire le rappel aux utilisateurs pour qu''ils puissent entreposer leurs données dans un endroit qui aura une telle copie.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Les sauvegardes doivent être faites de façon journalière pour éviter des pertes trop importantes.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Les sauvegardes doivent avoir une durée de rétention supérieure à 1 mois pour éviter les problèmes comme les crypto-ransomware.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Les sauvegardes doivent être délocalisées, dans la mesure du possible à plus de 3 kilomètres.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Les sauvegardes doivent être déconnectées, débranchées de l''infrastructure, au moins en partie, pour ne pas être détectables par des crypto-ransomware.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Les sauvegardes doivent être testées, pour s''assurer qu''elles sont bien faites et fonctionnelles.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Les sauvegardes doivent être chiffrées, particulièrement si elles sont déplacées.', 'fr', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'Pour le moment, la pratique de l''apport de matériel personnel (Bring Your Own Device) dans l''environnement professionnel n''est pas possible dans l''organisme. Si cela est néanmoins amené à changer un jour, il est important de faire attention:', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Le matériel personnel ne peut pas être utilisé dans un organisme sans contrôles et explications préalables. Les explications endiguent certaines attaques, particulièrement dès lors que la distinction des dangers et des choses qui peuvent arriver est faite.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Il doit être sous un contrôle antiviral pour s''assurer d''éviter un maximum d''infection sur le réseau.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Cette pratique nécessite des explications pour être comprise au mieux possible.', 'fr', 'R');



INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC001', 'Il est impératif de disposer d''une alimentation électrique de secours en cas de panne.', 'fr', 'R');
/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC002', 'Backup power supply can be a generator or any form of renewable energy such as solar energy.', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC003', 'L''alimentation de secours peut être un générateur ou toute forme d''énergie renouvelable comme l''énergie solaire.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC004', 'L''utilisation d''un onduleur fournit une source d''alimentation de secours sous la forme d''un système de stockage d''énergie pour maintenir la continuité de l''alimentation de la charge pendant que le système passe à l''alimentation de secours, évitant ainsi toute perte potentielle de données.', 'fr', 'R');

/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC001', '', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC002', 'La sécurité physique est aussi importante que la sécurité des informations et des systèmes, c''est pourquoi l''accès aux bureaux et aux salles de serveurs doit être accordé en fonction du profil de chaque personne.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC003', 'L''installation d''un système de vidéosurveillance est très efficace pour dissuader toute intention de vol.', 'fr', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC004', 'Les locaux de l''entreprise doivent être équipés des systèmes minimaux de détection et/ou de prévention des incendies.', 'fr', 'R');

-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'The company should define rules in order to avoid misunderstandings.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Rules (organisational, IT or working ones) should be known and explained to everyone, at the very least orally.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'If an oral transmission could be enough for a small company, rules should still be written in a charter, read and signed by everyone, very important if the company grows.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'An oral transmission could be a lot more complicated when there are lots of employees, and is really impossible when lots of people are hired and leaving.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Besides, written rules can :
	- avoid to forget some points
	- have a legal proof if the rules have been read.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'If it''s possible, rules should be as short and as easy as possible to be attractive and readable.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Rules that are too long or too heavy with technical vocabulary could become confusing.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Each time when it''s possible, some advice or some best practices should be given, and sometime explained.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Some differences might be appropriate depending on the role, or if it''s a temporary contract for instance.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'For the moment, the company does not have a lot of personal data, or haven''t done anything to it. If there is more personal data, or if nothing were done, the company should think:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Define, whenever possible, someone responsible for the personal data in order to avoid the lack of response when there is an incident.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Data Lifecycle should be accessible by everyone :
	- How they are obtained
	- How they are used
	- How they are accessible, by whom and the contract linked
	- How they are alterable
	- How much time they are stored
	- How they are destroyed
This cycle should be described somewhere and accessible by anyone (sell contracts, websites, files that could be shown ...).', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'People should know who is the responsible person for the data in order to ask all the necessary questions, requests and about data manipulation or data sensitivity.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'Concerning the image rights, some authorisations are required (to take an image and to diffuse it), and people need to know when a place is under video surveillance.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Updating the best practices for daily tasks is important to avoid all the basic mistakes and loss of time.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Learning to use software is important to avoid time loss, data loss and manipulation mistakes.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'By informing about attacks that are current, common or well-known, employees could more easily identify them and avoid falling for them.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Trainings that are done internally do not have the same impact as external ones, but could be more appropriate by the mastery of the subject within the company environment.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Train users on the sensitivity of the manipulated information, in order to put their attention on how to protect them.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'It''s important to define responsibilities, either externally or internally, with one person or more, or a company, but specialised into their own domain, with possibly a training.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'For now, no outside work is done. If it''s changed, it''s important to take care that:
	- External connections which are not controlled and monitored should be avoided to avoid data loss.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Whenever users have the need to work outside, from home office to missions outside the premises, they must have a VPN connection to connect to the server.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'External connection which is not controlled and monitored should be avoided to avoid data loss.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'The visual environment is really important, to avoid curiosity or spying.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Devices that are taken away and that contains confidential data should always have their internal memory encrypted to avoid data loss.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'For now, no contracts with third parties are signed. If it''s changed, it''s important to:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'If confidential data is accessible by different third parties, like external maintenace companies, or financial data by a fiduciary, a Non-Disclosure Agreement (NDA) should be signed with them.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'If means and needs permit it, a contract should be signed to ensure that the external IT provider will ensure the availability of system to remain operational.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'It''s necessary to review the contracts to ensuring a certain availability :
	- not having an intervention solution whenever it''s essential
	- to not pay too much for a service which is not necessary
	- to evaluate if the services paid are satisfying the necessary', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'For now, no third parties clean the premises. If it changes, it''s important to:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'The office cleaning should be done, whenever possible, during work time to avoid potential data theft.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Rules should be given mainly to specify what should be done or avoided.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'It''s important to define a confidentiality clause in all the contracts to ensure the confidentiality of information heard or seen.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'To avoid problems due to the human curiosity, it is important to have a clean desk policy to avoid confidential documents being seen.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'The staff shouldn''t clean restricted access areas, such as archive room or IT room.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Advice should be given to avoid weak passwords. Some tips or techniques could be given to employees to remember their passwords. Here some examples:
	- Passwords should be kept secret and personal. Each and everyone should access their data by using their password, even from a computer of someone else.
	- There shouldn''t be a computer which is shared with one and unique password. If it''s inevitable, then a trsutworthy person should be defined responsible, and access should be really limited.
	- It''s mandatory to be careful with the password storage in the internet browser as they are not protected.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Passwords should be kept secret and personal. If it''s impossible, then there should be a trustworthy person named responsible for the computer to ensure its use, and give minimum access.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Passwords should be kept secret and personal. Each and everyone should access their data by using their password, even from the computer of someone else.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'It''s necessary to have passwords which have at least one uppercase, lowercase, digit and special character, and a minimum of 12 characters.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Passwords shouldn''t be a coherent word or date, except if they are in a complete sentence.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Complete sentences could be used, even if they represent complete words.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Passwords should be changed from time to time, to prevent serious consequences in case of a leak.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'To make the storage easier, a password manager could be used.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'It''s mandatory to be careful with the password storage in the internet browser as they are not protected.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Same passwords used on different website makes a leak easier. Besides, only one leak is enough to compromise all the access using the same password.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'For now, wireless network isn''t activated in the company. If it is changed, it''s important to:
	- Wireless Network should be split between internal and external users to avoid access problems.
	- If a wireless network is used for external people, strong precautions should be taken, for example the collection of an identity.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Wireless Network should be split between internal and external users to avoid access problems.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'If a wireless network is used for external people, strong precautions should be taken, for example the collection of an identity', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'The password shouldn''t be easily guessable, to avoid connections which are not wanted.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Also, wireless networks of printers should be protected to avoid the leak of all printed documents.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'The company should have an anti-virus and be careful to:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'An anti-virus software must be on all devices.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'It should be up to date, preferably automatically to cover as many threats as possible.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'It should be activated in any case to protect the device continuously.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'All devices, like smartphones, tablets should have an anti-virus, even if it''s the one by default from the operating system.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Some tests should be done from time to time.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Some tests should be done in case of suspicion of infection.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Some rules and specific advice should be given concerning users stations or laptop. Some points that are important:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'A device should always be up to date in order to avoid security problems, and also avoid network intrusion. Many operating system now update automatically, but installed software needs some permission to be given or manual maintenance.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Administrator rights should be left only to the users who are specialised in IT, or welladvised respecting the rules.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Downloads should only be done from the official websites, the original developers of the software, to avoid illegal download or infections.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Devices should be locked to avoid identity theft.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'It''s important to have backups for various reason, to have redundancy of data if they disappeared. It''s important to have:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Backups should concern the whole company, and everyone should be aware to put all data on the systems that are backed up, to ensure to have a copy of them.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Backups should be done daily to avoid major data loss.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Backups should be retained at least a month to avoid problems caused by ransomware.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Backups should be outside the premises, decentralized, with more than 3 kilometres between them.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Backups should be disconnected, outside the local network, to be invisible by crypto-ransomwares.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Backups should be tested from time to time, just to ensure that the data is readable and has integrity.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Backups should be encrypted to avoid problems concerning the data theft, mainly if they are moved.', 'en', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'For now, the personal devices are not connected in the local network. If it''s changed, it''s important to:', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Personal devices shouldn''t be used in company without any controls, rules and explanations. By knowing all the different existing ways to attack an organism, it''s possible to avoid them', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Personal devices should have an antivirus installed, updated and active to avoid as many threats as possible.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Defining rules and best practices helps to protect the internal networks.', 'en', 'R');


INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC001', 'Having a backup power supply to switch to in case of an outage is imperative to insure business continuity.', 'en', 'R');
/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC002', 'Backup power supply can be a generator or any form of renewable energy such as solar energy.', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC003', 'Backup power supply can be a generator or any form of renewable energy such as solar energy.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC004', 'The usage of UPS for critical infrastructure systems is also important to maintain continuity of power to the respective load while the system is transitioning to backup power, hence preventing potential data loss.', 'en', 'R');

/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC001', '', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC002', 'The company''s premises should be equipped with the minimum fire detection and/or prevention systems.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC003', 'The installation of video surveillance system is very effective in deterring any intention of theft.', 'en', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC004', 'Physical security is as much important as information and systems security, hence access to the offices and server rooms must be granted based on the profile of each person.', 'en', 'R');


-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'Das Unternehmen sollte Regeln definieren, um Missverständnisse zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Regeln (organisatorische, IT- oder Arbeitsregeln) sollten zumindest mündlich bekannt sein und jedem erklärt werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'Wenn eine mündliche Übermittlung für ein kleines Unternehmen ausreichen könnte, sollten die Regeln dennoch in einer Charta festgehalten, von allen gelesen und unterzeichnet werden, was noch wichtiger wird, wenn das Unternehmen wächst.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'Eine mündliche Übermittlung könnte viel komplizierter sein, wenn es viele verschiedene Leute oder Arbeiten gibt, und ist wirklich unmöglich, wenn viel Personalwechsel existiert.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Außerdem können schriftliche Regeln:
	- dem Vergessen einiger Punkte vorbeugen
	- einen gesetzlichen Nachweis sein, wenn die Regeln gelesen und unterzeichnet wurden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'Wenn es möglich ist, sollten die Regeln so kurz und einfach wie möglich sein, um attraktiv und merbar zu sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Zu lange oder zu strenge Regeln mit technischem Vokabular können verwirrend wirken.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Jedes Mal, wenn es möglich ist, sollten einige Ratschläge oder Best Practices gegeben und gegebenenfalls erklärt werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Einige Unterschiede können je nach Rolle oder zum Beispiel bei einem befristeten Vertrag auftreten.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'Derzeit verfügt das Unternehmen nicht über personenbezogene Daten oder hat nichts dagegen unternommen. Wenn es doch personenbezogene Daten gibt oder wenn nichts unternommen wurde, sollte das Unternehmen folgende Überlegungen anstellen:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Definieren Sie, wann immer es möglich ist, jemanden, der für die personenbezogenen Daten verantwortlich ist, um zu vermeiden, dass ein Vorfall reaktionslos bleibt.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Der Datenlebenszyklus sollte für alle zugänglich sein:
	- Wie sie erhalten werden
	- Wie sie verwendet werden
	- Wie sind sie zugänglich, von wem und sind diese vertraglich geregelt
	- Wie sie veränderbar sind
	- Wie lange sind oder werden sie gespeichert
	- Wie sie zerstört werden
Dieser Zyklus sollte irgendwo beschrieben und für jeden zugänglich sein (Verkaufsverträge, Websites, Dateien, die angezeigt werden könnten ...).', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'Die Leute sollten wissen, wer der Verantwortliche ist, um alle notwendigen Fragen oder die Vertraulichkeit der Daten sicher zu stellen.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'In Bezug auf die Bildrechte müssen einige Autorisierungen angefragt werden (um ein Bild aufzunehmen und zu verbreiten), und die Leute sollten wissen, wann ein Ort unter Videoüberwachung steht.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Die Aktualisierung der Best Practices für die täglichen Aufgaben ist wichtig, um alle grundlegenden Fehler und Zeitverluste zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Das Erlernen des Gebrauchs von Software ist wichtig, um Zeitverlust, Datenverlust und Manipulationsfehler zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'Durch das Informieren über aktuelle, häufige oder bekannte Angriffe können Mitarbeiter diese leichter identifizieren und vermeiden, auf sie hereinzufallen.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Intern durchgeführte Schulungen haben nicht die gleichen Auswirkungen wie externe, könnten jedoch durch die Beherrschung des Fachs im Unternehmensumfeld angemessener sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Schulung der Benutzer in Bezug auf die Sensibilität der manipulierten Informationen, um ihre Aufmerksamkeit darauf zu lenken, wie sie geschützt werden sollen.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'Es ist wichtig, die Verantwortlichkeiten entweder extern oder intern mit einer oder mehreren Personen oder einem Unternehmen zu definieren, das jedoch auf seine eigene Domäne spezialisiert ist, möglicherweise mit einer Schulung.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'Im Moment wird keine Außenarbeit geleistet. Wenn es sich geändert hat, ist es wichtig darauf zu achten, dass:
- Externe Verbindungen, die nicht kontrolliert und überwacht werden, vermieden werden, um so Datenverlust zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Immer wenn Benutzer im Freien arbeiten müssen, vom Heimbüro bis zu Aufgaben außerhalb des Unternehmens, müssen sie über eine VPN-Verbindung verfügen, um eine Verbindung zum Server herstellen zu können.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'Externe Verbindungen, die nicht kontrolliert und überwacht werden, sollten vermieden werden, um Datenverlust zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'Die visuelle Umgebung ist sehr wichtig, um Neugierde und Spionage zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Bei Geräten, die entfernt wurden und vertrauliche Daten enthalten, sollte der interne Speicher immer verschlüsselt sein, um Datenverlust zu vermeiden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'Derzeit werden keine Verträge mit Dritten abgeschlossen. Wenn es sich geändert hat, ist es wichtig:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'Wenn verschiedene Dritte wie externe Wartungsunternehmen auf vertrauliche Daten für Finanzdaten eines Treuhänders zugreifen können, sollte mit ihnen eine Geheimhaltungsvereinbarung (Non Disclosure Agreement, NDA) unterzeichnet werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'Wenn Mittel und Bedürfnisse dies zulassen, sollte ein Vertrag unterzeichnet werden, um sicherzustellen, dass der externe IT-Anbieter die Verfügbarkeit des Systems sicherstellt, um betriebsbereit zu bleiben.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'Es ist notwendig, die Verträge zu überprüfen, um eine bestimmte Verfügbarkeit zu gewährleisten:
- keine Interventionslösung zu haben, wenn es notwendig ist
- nicht zu viel für eine Dienstleistung zu bezahlen, die nicht notwendig ist
- zu beurteilen, ob die bezahlten Leistungen den erforderlichen Anforderungen entsprechen', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'Derzeit reinigen keine Dritten die Räumlichkeiten. Wenn es sich ändert, ist es wichtig:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'Die Büroreinigung sollte nach Möglichkeit während der Arbeitszeit durchgeführt werden, um möglichen Datendiebstahl zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Regeln sollten hauptsächlich angegeben werden, um zu spezifizieren, was getan oder vermieden werden soll.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'Es ist wichtig, in allen Verträgen eine Vertraulichkeitsklausel zu definieren, um die Vertraulichkeit der gehörten oder gesehenen Informationen zu gewährleisten.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'Um Probleme aufgrund menschlicher Neugierde zu vermeiden, ist es wichtig, eine Richtlinie für saubere Schreibtische zu haben, um zu verhindern, dass vertrauliche Dokumente angezeigt werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'Das Personal sollte keine Bereiche mit eingeschränktem Zugang wie Archivräume oder IT-Räume reinigen.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Es sollten Hinweise gegeben werden, um schwache Passwörter zu vermeiden. Angestellte können Tipps oder Techniken erhalten, um sich ihre Passwörter zu merken. Hier einige Beispiele:
- Passwörter sollten geheim und persönlich gehalten werden. Jeder sollte mit seinem Passwort auf seine Daten zugreifen, auch von einem Computer eines anderen.
- Es sollte keinen Computer geben, auf dem ein einziges und eindeutiges Kennwort festgelegt ist. Wenn es unvermeidlich ist, sollte eine wahrheitsgemäße Person als verantwortlich definiert werden und der Zugang sollte wirklich eingeschränkt sein.
- Beim Speichern von Passwörtern im Internetbrowser ist Vorsicht geboten, da diese nicht geschützt sind.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Passwörter sollten geheim und persönlich gehalten werden. Wenn dies nicht möglich ist, sollte es eine vertrauenswürdige Person geben, die für den Computer verantwortlich ist, um dessen Verwendung zu gewährleisten und einen Mindestzugriff zu gewähren.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Passwörter sollten geheim und persönlich gehalten werden. Jeder sollte mit seinem Passwort auf seine Daten zugreifen, auch vom Computer einer anderen Person aus.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'Es sind Kennwörter mit mindestens einem Groß- und Kleinbuchstaben, einer Ziffer und einem Sonderzeichen sowie mindestens 12 Zeichen erforderlich.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Passwörter sollten kein zusammenhängendes Wort oder Datum sein, es sei denn, sie bestehen aus einem vollständigen Satz.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Es können vollständige Sätze verwendet werden, auch wenn sie vollständige Wörter beinhalten.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Passwörter sollten von Zeit zu Zeit geändert werden, um schwerwiegende Folgen im Falle eines Lecks zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'Um die Speicherung zu vereinfachen, könnte ein Passwort-Manager verwendet werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'Beim Speichern von Passwörtern im Internetbrowser ist Vorsicht geboten, da diese nicht geschützt sind.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Dieselben Passwörter, die auf verschiedenen Websites verwendet werden, erleichtern das Durchsickern. Außerdem ist nur ein Leck ausreichend, um den gesamten Zugriff mit demselben Kennwort zu gefährden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'Derzeit ist das drahtlose Netzwerk in der Firma nicht aktiviert. Wenn es geändert wird, ist es wichtig:
- Das drahtlose Netzwerk sollte zwischen internen und externen Benutzern aufgeteilt werden, um Zugriffsprobleme zu vermeiden.
- Wenn ein drahtloses Netzwerk für externe Personen verwendet wird, sollten strenge Vorsichtsmaßnahmen getroffen werden, z. B. das Sammeln einer Identität.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Das drahtlose Netzwerk sollte zwischen internen und externen Benutzern aufgeteilt werden, um Zugriffsprobleme zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'Wenn ein drahtloses Netzwerk für externe Personen verwendet wird, sollten strenge Vorsichtsmaßnahmen getroffen werden, z. B. das Sammeln einer Identität.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'Das Passwort sollte nicht leicht zu erraten sein, um unerwünschte Verbindungen zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Drahtlose Netzwerke von Druckern sollten ebenfalls geschützt werden, um das Auslaufen aller gedruckten Dokumente zu vermeiden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'Das Unternehmen sollte über ein Virenschutzprogramm verfügen und Folgendes beachten:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'Auf allen Geräten muss eine Antivirensoftware installiert sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'Es sollte auf dem neuesten Stand sein, vorzugsweise automatisch, um so viele Bedrohungen wie möglich abzudecken.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'Sie sollte auf jeden Fall aktiviert werden, um das Gerät dauerhaft zu schützen.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'Alle Geräte, wie Smartphones und Tablets, sollten mit einem Antivirenprogramm ausgestattet sein, auch wenn dieses standardmäßig vom Betriebssystem stammt.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Einige Tests sollten von Zeit zu Zeit durchgeführt werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Bei Verdacht auf eine Infektion sollten einige Tests durchgeführt werden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Einige Regeln und spezielle Ratschläge sollten in Bezug auf Benutzerstationen oder Laptops gegeben werden. Einige wichtige Punkte:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'Ein Gerät sollte immer auf dem neuesten Stand sein, um Sicherheitsprobleme und auch das Eindringen in das Netzwerk zu vermeiden. Viele Betriebssysteme werden jetzt automatisch aktualisiert, aber die installierte Software benötigt eine Erlaubnis oder manuelle Wartung.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Administratorrechte sollten nur Benutzern überlassen werden, die auf IT spezialisiert sind oder die die Regeln gut einhalten.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Downloads sollten nur von den offiziellen Websites, von den Originalentwicklern der Software, gemacht werden, um illegale Downloads oder Infektionen zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Geräte sollten gesperrt sein, um Identitätsdiebstahl zu vermeiden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'Es ist wichtig, Backups aus verschiedenen Gründen zu haben, damit die Daten redundant sind. Es ist wichtig zu haben:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Backups sollten das gesamte Unternehmen betreffen, und jeder sollte sich dessen bewusst sein, alle Daten auf den zu sichernden Systemen abzulegen, um sicherzustellen, dass eine Kopie davon vorliegt.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Backups sollten täglich durchgeführt werden, um Datenverluste zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Backups sollten mindestens einen Monat aufbewahrt werden, um Probleme durch Ransomware zu minimieren', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Backups sollten sich außerhalb der Räumlichkeiten befinden und mehr als 3 Kilometer voneinander entfernt sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Backups sollten außerhalb des lokalen Netzwerks und nach Abschluss vom System getrennt werden, damit sie von Cryptoransomware nicht erkannt werden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Backups sollten von Zeit zu Zeit getestet werden, um sicherzustellen, dass die Daten lesbar und integer sind.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Backups sollten verschlüsselt werden, um Probleme mit dem Datendiebstahl zu vermeiden, vor allem, wenn sie transportiert werden.', 'de', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'Derzeit sind die persönlichen Geräte nicht mit dem lokalen Netzwerk verbunden. Wenn es geändert wird, ist es wichtig:', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Persönliche Geräte sollten nicht ohne Kontrollen, Regeln und Erklärungen in der Firma verwendet werden. Wenn Sie die verschiedenen Möglichkeiten kennen, einen Organismus anzugreifen, können Sie Angriffe besser erkennen', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Auf persönlichen Geräten sollte ein Virenschutzprogramm installiert, aktualisiert und aktiviert sein, um so viele Bedrohungen wie möglich zu vermeiden.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Das Definieren von Regeln und Best Practices trägt zum Schutz der internen Netzwerke bei.', 'de', 'R');


INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC001', 'Eine Notstromversorgung, auf die man im Falle eines Stromausfalls umschalten kann, ist unerlässlich.', 'de', 'R');
/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC002', 'Backup power supply can be a generator or any form of renewable energy such as solar energy.', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC003', 'Die Notstromversorgung kann ein Generator oder eine Form von erneuerbarer Energie wie Solarenergie sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q014REC004', 'Die Verwendung von USV bietet eine Quelle für die Notstromversorgung in Form eines Energiespeichersystems, um die Kontinuität der Stromversorgung für die Last aufrechtzuerhalten, während das System auf die Notstromversorgung umschaltet, und somit einen möglichen Datenverlust zu verhindern.', 'de', 'R');

/*INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC001', '', 'en', 'R');*/
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC002', 'Die Räumlichkeiten des Unternehmens sollten mit einem Mindestmaß an Brandmelde- und/oder Brandschutzsystemen ausgestattet sein.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC003', 'Die Installation eines Videoüberwachungssystems ist ein sehr wirksames Mittel zur Abschreckung von Diebstahlsabsichten.', 'de', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q015REC004', 'Die physische Sicherheit ist ebenso wichtig wie die Informations- und Systemsicherheit, daher muss der Zugang zu den Büros und Serverräumen auf der Grundlage des Profils der einzelnen Personen gewährt werden.', 'de', 'R');

-- Update the sequences IDs
SELECT setval('survey_surveysection_id_seq', (SELECT MAX(id) from "survey_surveysection"));
SELECT setval('survey_surveyquestionservicecategory_id_seq', (SELECT MAX(id) from "survey_surveyquestionservicecategory"));
SELECT setval('survey_surveyquestion_id_seq', (SELECT MAX(id) from "survey_surveyquestion"));
SELECT setval('survey_surveyquestionanswer_id_seq', (SELECT MAX(id) from "survey_surveyquestionanswer"));
