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

/* survey_surveysection */
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (1, 'SECTION001OC');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (2, 'SECTION002GE');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (3, 'SECTION003GT');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (4, 'SECTION004AL');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (5, 'SECTION005RI');
INSERT INTO "survey_surveysection" ("id", "sectionTitleKey") VALUES (6, 'SECTION006IT');

/* survey_surveyquestion */
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (1, 'Q001RCHA', 'M', 10, 4, 1, 45);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (2, 'Q002GDPR', 'M', 20, 7, 1, 30);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (3, 'Q003TRAI', 'M', 30, 5, 2, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (4, 'Q004REIT', 'S', 40, 12, 2, 15);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (5, 'Q005TELE', 'M', 50, 9, 2, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (6, 'Q006SNDA', 'M', 60, 2, 3, 15);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (7, 'Q007CLEA', 'M', 70, 13, 3, 30);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (8, 'Q008PWDS', 'M', 80, 1, 4, 45);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (9, 'Q009WIFI', 'M', 90, 3, 5, 25);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (10, 'Q010AVIR', 'M', 100, 11, 5, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (11, 'Q011UPDT', 'M', 110, 10, 6, 35);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (12, 'Q012BACK', 'M', 120, 6, 6, 65);
INSERT INTO "survey_surveyquestion" ("id", "titleKey", "qtype", "qindex", "service_category_id", "section_id", "maxPoints") VALUES (13, 'Q013BYOD', 'M', 130, 8, 6, 20);

/* survey_surveyquestionanswer */
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
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (73, 'Q012A007', 70, 12, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (74, 'Q012A008', 80, 12, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (75, 'Q012A009', 90, 12, FALSE, 5);

INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (76, 'Q013A001', 10, 13, TRUE, 20);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (77, 'Q013A002', 20, 13, FALSE, 10);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (78, 'Q013A003', 30, 13, FALSE, 5);
INSERT INTO "survey_surveyquestionanswer" ("id", "answerKey", "aindex", "question_id", "uniqueAnswer", "score") VALUES (79, 'Q013A004', 40, 13, FALSE, 5);


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


/* survey_translationkey */
-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Mots de passe', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Contrats (SLA/NDA)', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'Wifi', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Règles/Chartes', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Formations', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Sauvegardes', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'GDPR', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Télétravail/Mobilité', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'Postes Utilisateurs/Mises à jour', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Antivirus', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'Responsabilités IT et Sécurité de l''Information', 'FR', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Nettoyage des Locaux', 'FR', 'C');
-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Passwords', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Contracts (SLA/NDA)', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'WiFi', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Rules/Charter', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Trainings', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Backups', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'GDPR', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Home Office/Mobility', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'User Work Stations/Updates', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Anti-virus', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'IT and Information Security Responsibilities', 'EN', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Office Cleaning', 'EN', 'C');
-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT001PWDS', 'Passwörter', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT002SNDA', 'Verträge (SLA/NDA)', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT003WIFI', 'WLAN', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT004RCHA', 'Regeln/Charter', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT005TRAI', 'Schulungen', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT006BACK', 'Backup', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT007GDPR', 'DSGVO', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT008BYOD', 'BYOD', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT009TELE', 'Heimarbeit/Mobilität', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT010UPDT', 'Benutzerarbeitsplätze/Updates', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT011AVIR', 'Antivirus', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT012REIT', 'Verantwortlichkeiten für Anti-VirusIT und Informationssicherheit', 'DE', 'C');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SERVCAT013CLEA', 'Büroreinigung', 'DE', 'C');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Obligations et Conformités', 'FR', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Gestion des Employés', 'FR', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Gestion des Tiers', 'FR', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Accès Logiques', 'FR', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Réseau Interne', 'FR', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Infrastructure IT', 'FR', 'S');
-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Awareness and Compliance', 'EN', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Employee Management', 'EN', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Third Party Management', 'EN', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Logical Access', 'EN', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Local Area Network', 'EN', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Information System', 'EN', 'S');
-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION001OC', 'Bewusstsein und Konformität', 'DE', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION002GE', 'Verwaltung von Mitarbeiter', 'DE', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION003GT', 'Verwaltung von Dritte', 'DE', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION004AL', 'Logischer Zugriff', 'DE', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION005RI', 'Lokales Netzwerk', 'DE', 'S');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('SECTION006IT', 'Informationssystem', 'DE', 'S');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'Dans l''entreprise, les règles données aux employés sont', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'non décrites', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'transmises oralement à toutes et tous', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'écrites et données par mail', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'lues et signées par tous, et inscrites dans une charte', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'écrites/expliquées avec du vocabulaire simple, non spécifique à un métier', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'assez longues, mais très précises', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'données avec des conseils et des bonnes pratiques pour faciliter la vie des employés', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'adaptées selon la personne la personne et/ou son rôle', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'Dans l''entreprise, sont défini', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'aucune autre donnée personnelle que celles des employés, ou aucune gestion concernant les données personnelles', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'une personne responsable de toutes les actions liées aux données personnelles', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'une explication écrite sur le cycle de vie des données internes (comment elles sont récupérées, comment elles sont stockées, où et quand elles sont détruites...)', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'une explication orale ou écrite pour les employés sur le comportement à adopter pour les cas concernant les données personnelles', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'une vidéosurveillance ou une prise d''image comme donnée personnelle, particulièrement si elle contient une personne ou une identité avec un lieu', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Les employés sont formés', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'à leur métier par leurs études ou cursus scolaire, mais aussi avec des formations supplémentaires pour mettre à jour les connaissances', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'aux logiciels qu''ils utilisent quotidiennement', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'à la sécurité de l''information pour avoir les clés en main afin de se défendre contre d''éventuelles attaques', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'en interne ou en externe par des spécialistes', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'et sensibilisés à l''importance de conserver confidentiellement les données, particulièrement si elles sont personnelles', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'Les responsabilités IT et Sécurité de l''Information', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'sont définis en interne, avec une personne spécialisée à régler les problèmes informatiques', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'sont définis en interne, avec deux personnes aux formations et métiers spécialisés dans le domaine', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'sont définis en externe, par un contrat', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'sont définis en externe, sur demande selon les besoins, sans contrat pour lier les entreprises', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'ne sont pas définis; chacun résout son problème ou fait appel à un autre employé avec plus de compétence dans le domaine', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'Les employés, lors d''un voyage à l''extérieur, utilisent', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'aucun appareil professionnel, car le télétravail n''est pas une pratique autorisée et la seule connexion possible au réseau d''entreprise est interne', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'un VPN (Virtual Private Network) est utilisé pour chiffrer les données lors de toute connexion sur le serveur interne de l''entreprise', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'un WiFi public, une connexion ouverte, ou une connexion protégée par mot de passe d''un organisme ou d''une personne externe', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'une connexion privée ou du partage de réseau d''un téléphone personnel ou professionnel', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'un filtre à écran, ou portent une attention particulière à la vision possible sur les écrans au travers des fenêtres ou dans les transports publics', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'un matériel avec un stockage de données chiffré ou sans données confidentielles pour éviter toute perte involontaire de données', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Des contrats avec les différents prestataires (informatique, comptabilité...)', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'ne sont pas définis, et ces derniers n''interviennent uniquement en cas de besoin de façon ponctuelle', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'définissent la confidentialité des données et la protection nécessaire de ces dernières', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'définissent le temps maximum pour lequel ces derniers doivent intervenir', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'sont régulièrement revus pour s''assurer qu''ils correspondent toujours aux besoins', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'Le nettoyage des locaux de travail se déroule', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'en interne, par les employés, de façon ponctuelle', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'pendant les heures de bureau', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'sous couvert de règles données concernant ce qu''il faut éviter de faire, ou éviter de toucher', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'sous couvert d''un contrat spécifiant la confidentialité à respecter', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'alors que tous documents confidentiels sont verrouillés à clé, dans des armoires, des bureaux, ou une salle spécifique', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'en évitant les salles ou les accès sont interdits, comme une salle d''archive ou une salle serveur', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Les mots de passe dans l''entreprise', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'ne sont pas soumis à des consignes ou conseils particuliers, ou sont laissés à discrétion de chacun', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'sont centralisés dans un fichier, ou tous connus par une ou plusieurs personnes', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'sont partagés selon le besoin d''accéder à une machine', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'font 12 caractères ou plus, et possèdent au moins une majuscule, une minuscule, un chiffre et un caractère spécial', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'ne forment pas des mots ou des dates cohérentes', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'sont des phrases complètes', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'sont changés régulièrement, tous les ans ou tous les deux ans', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'sont inclus dans un gestionnaire de mots de passe', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'sont sauvegardés dans les navigateurs Web', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'sont différents pour chaque application, même pour un utilisateur', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Les réseaux sans fil', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'ne sont pas activés dans l''organisme', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'sont utilisés sans distinctions par des externes comme des personnes internes à l''entreprise', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'sont donnés sans distinctions à des externes comme des personnes internes à l''organisme et sans récolte d''identité', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'sont protégés par des mots de passe très longs (plus de 20 caractères) différents de celui par défaut', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'des imprimantes sont protégées par un mot de passe', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Un logiciel antivirus', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'n''est pas installé ou utilisé', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'est installé sur toutes les machines de bureau et les ordinateurs portables', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'est mis à jour sur toutes les machines, de façon automatique comme manuelle', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'est activé et protège les machines de façon proactive', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'est installé sur tous les téléphones mobiles étant sur le réseau', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'est utilisé de temps à autre pour analyser la bonne santé d''une machine, même sans évènements externes', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'est utilisé pour analyser le réseau en cas de suspicion d''infection', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'Les postes utilisateurs sont', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'laissés sans consignes à discrétion des utilisateurs', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'mis à jour de façon automatique ou manuelle (logiciels comme système d''exploitation)', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'soumis aux droits d''administration, qui empêche pour tout utilisateur d''installer un logiciel', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'soumis à des règles et des consignes en ce qui concerne l''installation et le téléchargement de programme, comme sur l''illégalité, ou éviter d''installer sans faire attention', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'verrouillés en cas d''une brève absence, même pour en temps très court', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Les sauvegardes sont', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'inexistantes: elles ne sont pas faites ou non fonctionnelles', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'transférées: le prestataire informatique en a la responsabilité à travers le Cloud', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'exhaustives: toutes les données qui doivent être incluses dans les sauvegardes, et tous les utilisateurs en sont conscients et ne stockent pas de données en local', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'journalières: les sauvegardes sont faites tous les jours ou plus', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'retenues: il est possible de remonter dans le temps dans les sauvegardes à 1 mois ou plus ', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'délocalisées: le serveur et les sauvegardes ne sont pas au même endroit, à plus de 3 kilomètres de distance', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'déconnectées: au moins en partie débranchées du serveur une fois qu''elles ont été faites', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'testées: un ou plusieurs fichiers sont restaurés à partir d''une sauvegarde de temps en temps', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'chiffrées: si elles sont amenées en dehors de l''entreprise, elles doivent être illisibles', 'FR', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'La pratique d''amener du matériel personnel informatique (Clé USB, disque dur, mobile, tablette, laptop ...) dans l''environnement professionnel (réseau qui se connecte au serveur)', 'FR', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'est interdite ou impossible dans l''organisme', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'est soumise à des règles précises, particulièrement en cas d''insertion sur le réseau interne de l''organisme', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'est soumise à un contrôle strict', 'FR', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'a été expliquée aux employés à travers des formations ou des explications', 'FR', 'A');
-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'In the company, rules are', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'not described', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'orally given', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'written and given by mail', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'read and signed by everyone, in a user charter', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'written and explained with simple words, which are non-specific to a type of work', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'quite heavy, but really accurate', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'given with advice and the best practices', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'adapted depending on the role of the reader', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'In the company, there is/are', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'no personal data other than the employee data, or nothing related to the personal data', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'someone who does every action bound to personal data', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'a written explanation about the personal data lifecycle (how there are get, stored, and when and how they are destroyed)', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'an oral or a written explanation of what should be done when there is a problem with personal data', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'some video surveillance, or some pictures taken, that contains face or people and possibly location data', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Employees are trained for/in', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'their work, their daily tasks by their studies, but also receive trainings to update their knowledge', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'the software they daily use', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'information security, to have the knowledge to protect themselves against attacks', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'by specialists, that could be internal or external', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'the importance to keep confidential data confidential, and more importantly if they are personal', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'IT and Information Security responsibilities are:', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'internally defined, with someone who is specialised in IT field', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'internally defined, with at least two persons that were trained on the field', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'externally defined, with a contract', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'externally defined, depending on the needs, without any contract specified', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'aren''t defined; anyone tries to resolve their problems, asking to someone else if they can', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'During any trip outside the company, employee uses', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'no professional tools because home office or travel is not allowed or necessary, or the only connection to the internal network is on the company premises', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'VPN (Virtual Private Network) is used to cipher all data from any network to the internal server', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'public Wi-Fi, open networks or connection protected by external organisation or person', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'a private connection or a connection sharing from a private or professional smartphone', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'a screen filter or their attention to ensure that no non-authorised person could see what is on the screen', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'devices that are ciphered (protected by a password at boot) or without any confidential data', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Contracts that are signed with third parties', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'are not defined, because they only come punctually in case of an incident or needs', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'define confidentiality of data, and their protection', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'define the maximum time of intervention after an incident', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'are regularly reviewed to ensure that they correspond to the needs', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'The office cleaning is done', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'internally, by employees, punctually', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'during the work time', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'under rules of what should be done and what shouldn''t be done', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'under a contract which specifies confidentiality of a contract', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'with all confidential documents locked under a room, a desk or a closet', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'done avoiding rooms which as restrained access, like an archive room or a server room', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Passwords in the company are', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'not under some advice or guidelines, or let to employees', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'centralised in a file, or all known by one or more people', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'shared whenever there is a need to access to a protected device', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'made of 12 or more letters which are uppercase, lowercase, digits and special character', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'do not form any words or dates', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'complete sentences', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'regularly changed, every year or two years', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'included in a password manager', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'included in web browsers', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'different for each application used, even for one user', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Wireless networks', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'are not used in the company', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'are used by everyone and access is granted to the company server', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'are given to everyone, without any way to get identity of the persons', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'are protected by long passwords of 20 characters or more', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'of the printers are protected by a strong password', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Antivirus software', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'are not installed or used', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'is installed on computers and laptops', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'is updated on all computers, automatically or manually', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'is activated and protect computers', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'is installed on all mobile phones that are on networks', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'is used from time to time in order to analyse the computer, even without external events', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'is used to analyse the network whenever a suspicious event occurs', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'The user workstations are', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'let without any rules, and users have to take care of their computer', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'automatically or manually updated, software as operating system', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'under administration rights, which won''t let users install software', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'under rules or advice that about installation and downloading software, concerning illegality or the danger to install something without authorisation', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'locked whenever the user is not at his desk, even for a short time', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Backups are', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'not existed: they are not done or not working', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'shared: a third party as the responsibility of the backup', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'exhaustive: all data should be in backups, and all users know it, and avoid storing it locally', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'daily done: backups are made every day or more', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'retained: it should be possible to get back a month before or more', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'dislocated: the server, and at least a complete backup are separated by 3 kilometres', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'disconnected: they are disconnected from the server once they are done', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'tested: one or all the files are restored from a backup from time to time', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'ciphered: when they are brought outside the company, they can''t be read', 'EN', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'Having some personal IT devices (USB Key, Hard Drive, Smartphone, Tablet, Laptop ...) in the professional environment (network that is connected to the server)', 'EN', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'is forbidden or impossible in the company', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'is under precise rules, particularly before connecting to the company network', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'is under a strict anti-virus control', 'EN', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'has been explained to employees through training or explanations', 'EN', 'A');
-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001RCHA', 'In der Firma werden Regeln', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A001', 'nicht beschrieben', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A002', 'mündlich übertragen', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A003', 'geschrieben und per Mail mitgeteilt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A004', 'von allen gelesen und unterschrieben und in einer Benutzercharta festgehalten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A005', 'geschrieben und erklärt mit einfachen Worten, die unabhängig des Arbeitsbereiches sind', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A006', 'ziemlich schwer, aber sehr genau', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A007', 'mit Rat und den besten Praktiken übermittelt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001A008', 'angepasst je nach Rolle des Lesers', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002GDPR', 'In der Firma gibt es / sind', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A001', 'keine personenbezogenen Daten als die der Angestellten oder keine personenbezogenen Daten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A002', 'jemand, der jede an persönliche Daten gebundene Handlung ausführt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A003', 'eine schriftliche Erklärung über den Lebenszyklus personenbezogener Daten (wie sie abgerufen, gespeichert und wann und wie sie vernichtet werden)', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A004', 'eine mündliche oder schriftliche Erklärung, was zu tun ist, wenn es ein Problem mit personenbezogenen Daten gibt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002A005', 'einige Videoüberwachungen oder einige aufgenommene Bilder, die Gesichter oder Personen enthalten, die allen erklärt werden', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003TRAI', 'Die Mitarbeiter sind ', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A001', 'geschult um ihre Arbeit, ihre täglichen Aufgaben zu bewältigen; durch ihr Studium, aber auch durch regelmäßge Fortbildung', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A002', 'geschult um die Software, die sie täglich brauchen benutzen zu können', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A003', 'geschult in Informationssicherheit, um sich vor Angriffen schützen zu können', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A004', 'von internen oder externen Spezialisten geschult.', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003A005', 'geschult die Wichtigkeit zu erkennen, einige Daten vertraulich zu behandeln, persönliche Daten inklusive', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REIT', 'IT- und Informationssicherheitsaufgaben sind:', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A001', 'intern definiert, mit jemandem, der im IT-Bereich spezialisiert ist', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A002', 'intern definiert, mit mindestens zwei Personen, die auf dem Feld geschult wurden', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A003', 'extern definiert, mit einem Vertrag', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A004', 'extern definiert, je nach Bedarf, ohne Angabe eines Vertrages', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004A005', 'sind nicht definiert; Jeder versucht, seine Probleme zu lösen und fragt jemanden, ob er kann', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005TELE', 'Während einer Reise außerhalb des Unternehmens verwendet der Mitarbeiter', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A001', 'Keine professionellen Werkzeuge, da Home Office oder Reisen nicht zulässig oder erforderlich sind oder die einzige Verbindung zum internen Netzwerk auf dem Firmengelände besteht', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A002', 'VPN (Virtuelles privates Netzwerk) wird verwendet, um alle Daten von einem beliebigen Netzwerk zum internen Server zu verschlüsseln', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A003', 'öffentliches WLAN, offene Netzwerke oder Verbindungen, die durch eine externe Organisation oder Person geschützt sind', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A004', 'a private connection or a connection sharing from a private or professional smartphone', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A005', 'einen Bildschirmfilter oder deren Aufmerksamkeit, um sicherzustellen, dass keine nicht autorisierte Person sehen kann, was sich auf dem Bildschirm befindet', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005A006', 'Geräte, die verschlüsselt (durch ein Passwort beim Booten geschützt) oder ohne vertrauliche Daten sind', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006SNDA', 'Verträge, die mit Dritten geschlossen werden', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A001', 'sind nicht definiert, weil sie nur im Falle eines Ereignisses oder Bedarfs pünktlich eintreffen', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A002', 'Vertraulichkeit von Daten und deren Schutz definieren', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A003', 'Definieren Sie die maximale Eingriffszeit nach einem Vorfall', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006A004', 'werden regelmäßig überprüft, um sicherzustellen, dass sie den Bedürfnissen entsprechen', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007CLEA', 'Die Büroreinigung ist erledigt', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A001', 'intern, von Mitarbeitern, pünktlich', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A002', 'während der Arbeitszeit', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A003', 'nach Regeln, was getan werden soll und was nicht', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A004', 'gemäß einem Vertrag, der die Vertraulichkeit eines Vertrags festlegt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A005', 'Alle vertraulichen Dokumente sind unter einem Raum, einem Schreibtisch oder einem Schrank eingeschlossen', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007A006', 'Vermeidung von Räumen, die als beschränkt zugänglich sind, wie ein Archivraum oder ein Serverraum', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008PWDS', 'Passwörter in der Firma sind', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A001', 'nicht unter einigen Ratschlägen oder Richtlinien, oder an Mitarbeiter vermieten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A002', 'zentralisiert in einer Datei oder alle, die einer oder mehreren Personen bekannt sind', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A003', 'freigegeben, wenn auf ein geschütztes Gerät zugegriffen werden muss', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A004', 'aus 12 oder mehr Buchstaben bestehend aus Groß- und Kleinbuchstaben, Ziffern und Sonderzeichen', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A005', 'Bilden Sie keine Wörter oder Daten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A006', 'vollständige Sätze', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A007', 'regelmäßig gewechselt, jedes Jahr oder zwei Jahre', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A008', 'in einem Passwort-Manager enthalten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A009', 'in Webbrowsern enthalten', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008A010', 'für jede verwendete Anwendung unterschiedlich, auch für einen Benutzer', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009WIFI', 'Drahtlose Netzwerke', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A001', 'werden im Unternehmen nicht verwendet', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A002', 'werden von allen genutzt und der Zugriff auf den Unternehmensserver gewährt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A003', 'werden jedem gegeben, ohne die Identität der Personen zu bekommen', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A004', 'sind durch lange Passwörter mit mindestens 20 Zeichen geschützt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009A005', 'der Drucker sind durch ein starkes Passwort geschützt', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010AVIR', 'Antiviren Software', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A001', 'nicht installiert oder verwendet werden', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A002', 'ist auf Computern und Laptops installiert', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A003', 'wird auf allen Computern automatisch oder manuell aktualisiert', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A004', 'ist aktiviert und schützt Computer', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A005', 'ist auf allen Mobiltelefonen in Netzwerken installiert', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A006', 'wird von Zeit zu Zeit verwendet, um den Computer auch ohne externe Ereignisse zu analysieren', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010A007', 'wird verwendet, um das Netzwerk zu analysieren, wenn ein verdächtiges Ereignis auftritt', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011UPDT', 'Die Benutzerarbeitsplätze sind', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A001', 'Lassen Sie ohne Regeln, und Benutzer müssen sich um ihren Computer kümmern', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A002', 'automatisch oder manuell aktualisiert, Software als Betriebssystem', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A003', 'unter Administrationsrechten, mit denen Benutzer keine Software installieren können', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A004', 'nach Regeln oder Ratschlägen, die über die Installation und das Herunterladen von Software, die Rechtswidrigkeit oder die Gefahr der unbefugten Installation von etwas informieren', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011A005', 'gesperrt, wenn der Benutzer nicht an seinem Schreibtisch ist, auch nur für kurze Zeit', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012BACK', 'Backups sind', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A001', 'nicht existiert: sie sind nicht fertig oder funktionieren nicht', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A002', 'geteilt: ein Dritter als die Verantwortung für die Sicherung', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A003', 'Vollständig: Alle Daten sollten sich in Backups befinden und allen Benutzern bekannt sein. Vermeiden Sie es, sie lokal zu speichern', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A004', 'Täglich erledigt: Backups werden jeden Tag oder mehr erstellt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A005', 'Beibehalten: Es sollte möglich sein, einen Monat vorher oder später zurückzukehren', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A006', 'Verlegt: Der Server und mindestens ein vollständiges Backup sind 3 Kilometer voneinander entfernt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A007', 'disconnected: Sie werden vom Server getrennt, sobald sie fertig sind', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A008', 'Geprüft: Von Zeit zu Zeit werden eine oder alle Dateien aus einem Backup wiederhergestellt', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012A009', 'verschlüsselt: Wenn sie aus dem Unternehmen gebracht werden, können sie nicht gelesen werden', 'DE', 'A');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013BYOD', 'Einige persönliche IT-Geräte (USB-Stick, Festplatte, Smartphone, Tablet, Laptop ...) im professionellen Umfeld (Netzwerk, das mit dem Server verbunden ist) haben', 'DE', 'Q');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A001', 'ist in der Firma verboten oder unmöglich', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A002', 'is under precise rules, particularly before connecting to the company network', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A003', 'unterliegt einer strengen Virenschutzkontrolle', 'DE', 'A');
    INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013A004', 'wurde den Mitarbeitern durch Schulungen oder Erklärungen erklärt', 'DE', 'A');

-- FR
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'L''entreprise doit définir des règles pour éviter toutes incompréhensions.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Les règles (qu''elles soient organisationnelles, métier, ou à l''usage de l''informatique) doivent être connues et expliquées à tous, au moins oralement au possible.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'Si une transmission orale suffit dans un cadre "familial", les règles devraient être mises dans une charte ou un règlement, écrites et signées par tous, particulièrement en cas de croissance.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'Une transmission uniquement orale peut rapidement devenir compliquée quand il y a beaucoup de personnes, et devient vite ingérable lors des phases de départ et d''arrivée du personnel importante.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Les règles écrites et signées ont l''avantage :
	- d''éviter les oublis.
	- d''avoir une preuve juridique que les règles sont connues.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'Dans la mesure du possible, ses dernières doivent être simples et courtes surtout pour être attractive et lisible.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Des règles trop longues ou trop lourdes de vocabulaire technique pourront devenir confuses pour les employés.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Si possible, il ne faut pas hésiter à donner des astuces pour aider au respect des règles, voire parfois, expliquer en quoi elles sont nécessaires.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Aussi, des petites adaptations doivent être pensées selon le rôle, ou si le contrat est temporaire par exemple.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'Pour le moment l''entreprise ne dispose que peu de données personnelles. Cependant, particulièrement si le nombre de traitements auguemente, ou si rien de particulier n''a été fait, il faut penser:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Définir, dans la mesure du possible, une personne qui est responsable de la gestion des données pour éviter le manque de réponse en cas d''incident.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Le cycle de vie des données personnelles doit être accessible pour n''importe qui (registre de traitement) ;
	- Comment sont-elles obtenues ?
	- Comment sont-elles traitées ?
	- Comment sont-elles accessibles et par qui, sous quelles clauses ?
	- Comment sont-elles modifiables ?
	- Combien de temps sont-elles conservées ?
	- Comment sont-elles détruites ?
Ce cycle devrait être décrit quelque part et accessible à tous (contrat de vente, site web, fichier présentable en cas d''interrogation ...).', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'Dans l''idéal, les employés, principalement au contact des clients, doivent connaître la personne responsable pour renvoyer correctement la requête, mais aussi la sensibilité des données manipulées.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'Une autorisation doit être demandée pour le droit à l''image (droit de prendre le cliché comme sa diffusion), et les personnes doivent être conscientes d''une vidéosurveillance.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Les formations métier sont importantes et doivent être mises régulièrement à jour pour s''assurer d''avoir les dernières pratiques et éviter les pertes de temps inutiles.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Des formations sur les logiciels utilisés de façon quotidienne évitent principalement les mauvaises gestions et les erreurs de manipulations.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'S''informer sur les différents types d''attaques existants et les moyens pouvant mis être en œuvre pour une attaque permet au possible d''éviter des comportements menant à la réussite de ces dernières.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Des formations faites en interne n''ont parfois pas le même impact que celles faites en externe, mais sont tout aussi valables, et parfois même plus appropriées pour la maîtrise du sujet et de la bonne orientation du discours.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Sensibiliser les utilisateurs à la sensibilité des informations manipulés pour attirer leur attention sur les protections à mettre en œuvre.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'Il est important de définir les responsabilités, que ce soit en interne ou en externe, avec une ou plusieurs personnes, ou une entreprise vraiment spécialisée dans le domaine de la responsabilité, avec au possible une formation.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'Pour le moment, aucun travail à l''extérieur n''est fait. Si cela est néanmoins amené à changer à jour, il est important de faire attention :
	- Les connexions extérieures non contrôlées doivent être évitées pour éviter d''éventuelles pertes de données.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Quand une connexion est faite de l''extérieur vers l''entreprise, il est important d''accéder au réseau interne par l''intermédiaire d''un VPN pour s''assurer que les données restent confidentielles.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'Les connexions extérieures non contrôlées doivent être évitées pour éviter d''éventuelles pertes de données.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'Une attention particulière doit être apportée à l''environnement visuel pour éviter les regards indiscrets ou de l''éventuel espionnage.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Le matériel doit être chiffré s''il contient des données confidentielles pour éviter toute perte de confidentialité.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'Pour le moment, aucun contrat avec les prestataires n''est signé. Si cela est néanmoins amené a changer à jour, il est important de faire attention:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'Si des données confidentielles sont accessibles par différents prestataires, par exemple des données financières par une fiduciaire, ou des données sur un serveur accessible à un prestataire informatique, il est nécessaire de les protéger avec un contrat de confidentialité.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'Si les moyens et le contexte le permettent et le nécessitent, un contrat est nécessaire pour assurer la disponibilité, tant les informations nécessaires, que le matériel pour les manipuler.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'Il faut régulièrement revoir les contrats assurant une certaine disponibilité pour s''assurer:
	- de ne pas se retrouver sans intervention dans un délai où cette dernière serait indispensable;
	- de ne pas surpayer un prestataire pour un temps d''intervention trop élevé;
	- que les services rendus sont d''un niveau de qualité suffisant à ce qui est nécessaire.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'Pour le moment, aucun prestataire ne réalise le nettoyage des locaux. Si cela est néanmoins amené a changer à jour, il est important de faire attention:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'Le nettoyage des locaux doit se faire, dans la mesure du possible, pendant les heures de bureau pour éviter des éventuels vols de données.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Des règles doivent être données pour principalement spécifier ce qu''il faut faire où éviter de toucher.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'Il faut également un contrat de confidentialité, car il est souvent possible d''entendre ou de remarquer des données confidentielles, même si l''accès n''est pas spécifiquement officiel.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'Pour éviter les problèmes de curiosité humaine, les documents confidentiels doivent être inaccessibles, surtout à première vue.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'Le personnel d''entretien ne doit pas intervenir dans un local à accès restreint, comme une salle d''archive ou une salle serveur.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Il est nécessaire de donner des consignes pour éviter les mots de passe faibles. Des astuces et techniques peuvent être données pour éviter l''oubli fréquent de ces derniers. En voici quelques exemples :
	- Les mots de passe doivent être personnels, et personne d''autre ne doit en avoir la connaissance. En cas de besoin, chacun doit pouvoir accéder aux fichiers à partir de son mot de passe personnel.
	- Il faut éviter d''avoir une machine accessible par un seul et unique accès, et partagée. Si c''est inévitable, alors il est nécessaire de définir un responsable de cette machine, chargé d''en assurer sa bonne utilisation, et de donner les accès les plus limités possible.
	- Les navigateurs internet ne stockent pas les mots de passe de façon protégés, et cette fonctionnalité est donc à éviter.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Ces derniers doivent également être personnels, et personne d''autre ne doit en avoir la connaissance. En cas de besoin, chacun doit pouvoir accéder aux fichiers à partir de son mot de passe personnel.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Il faut éviter d''avoir une machine accessible par un seul et unique accès. Si c''est inévitable, alors il est nécessaire de définir un responsable de cette machine, chargé d''en assurer sa bonne utilisation, et de donner les accès les plus limités possible.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'Il est nécessaire d''avoir des mots de passe ayant au moins une majuscule, une minuscule, un chiffre et un caractère spécial, pour un total de 12 caractères ou plus.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Les mots de passe ne doivent pas former des mots ou des dates cohérentes pour qu''ils ne soient pas facilement devinables.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Des phrases complètes peuvent être utilisées comme mot de passe, même s''ils forment des mots complets.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Les mots de passe doivent être changés de temps à autre pour prévenir une possible fuite de ses dernières.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'Des gestionnaires de mot de passe peuvent être utilisés pour faciliter la gestion et leur stockage.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'Les navigateurs internet ne stockent pas les mots de passe de façon protégés, et cette fonctionnalité est donc à éviter.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Les mots de passe réutilisés dans d''autres sites offrent plus de chance de divulgation. De plus, une seule perte de mot de passe suffit à compromettre la totalité des accès.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'Pour le moment, les réseaux sans fil ne sont pas activés dans l''entreprise. Si cela est néanmoins amené à changer à jour, il est important de faire attention:
	- Dans l''idéal, les réseaux sans fil doivent être séparés entre les utilisateurs externes et internes pour éviter de nombreux problèmes d''accès.
	- Si un réseau sans fil pour des personnes externes, des protections lourdes doivent être mises en place, comme une récolte d''identité pour désigner le responsable d''une connexion à du contenu qui outrepasserait le cadre légal.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Dans l''idéal, les réseaux sans fil doivent être séparés entre les utilisateurs externes et internes pour éviter de nombreux problèmes d''accès.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'Si un réseau sans fil pour des personnes externes, des protections lourdes doivent être mises en place, comme une récolte d''identité pour désigner le responsable d''une connexion à du contenu qui outrepasserait le cadre légal.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'Le mot de passe du réseau sans fil ne doit pas être facilement devinable pour éviter des connexions non désirées.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Les réseaux WiFi d''imprimante, s''ils sont nécessaires, doivent être protégés pour éviter toute fuite des documents imprimés et scannés.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'L''entreprise doit se munir d''antivirus, et faire attention:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'Un logiciel antivirus doit être installé sur les machines pour empêcher au maximum possible les infections virales.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'Ce dernier doit être mis à jour, au moins de façon automatique pour couvrir le plus de menaces possible.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'Il doit être également activé en permanence pour protéger en continu la machine.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'Tout appareil, y compris des appareils plus nomades comme les ordinateurs portables, les téléphones et les tablettes doivent avoir un antivirus, même ceux proposés par défaut dans les systèmes d''exploitation.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Dans l''idéal, il ne faut pas hésiter à faire des tests de temps à autre.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Des tests doivent être réalisés dès lors d''une suspicion d''infection.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Des consignes et un encadrement précis doivent être donnés aux utilisateurs de station de travail. Voici des points à donner:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'Une machine doit être le plus à jour possible pour éviter le plus de failles, et ainsi éviter au possible les attaques par intrusion dans le réseau. Si beaucoup de systèmes d''exploitation se mettent à jour sans aide particulière, les logiciels doivent recevoir une attention particulière.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Les droits d''administration peuvent être laissés à des utilisateurs avertis et informés des consignes pour utiliser leur machine, mais nécessitent des règles précises.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Les téléchargements doivent être sur les sites officiels, tant pour éviter d''éventuels téléchargements illégaux que les différents virus, et ces consignes doivent être données.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Les machines doivent être verrouillées pour éviter toute usurpation d''identité.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'Il est important d''avoir des sauvegardes pour de nombreuses raisons, comme s''assurer d''avoir une redondance des données. Il est important d''avoir et de respecter:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Les sauvegardes doivent concerner toutes les données de l''entreprise, et il est important d''en faire le rappel aux utilisateurs pour qu''ils puissent entreposer leurs données dans un endroit qui aura une telle copie.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Les sauvegardes doivent être faites de façon journalière pour éviter des pertes trop importantes.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Les sauvegardes doivent avoir une durée de rétention supérieure à 1 mois pour éviter les problèmes comme les crypto-ransomware.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Les sauvegardes doivent être délocalisées, dans la mesure du possible à plus de 3 kilomètres.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Les sauvegardes doivent être déconnectées, débranchées de l''infrastructure, au moins en partie, pour ne pas être détectables par des crypto-ransomware.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Les sauvegardes doivent être testées, pour s''assurer qu''elles sont bien faites et fonctionnelles.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Les sauvegardes doivent être chiffrées, particulièrement si elles sont déplacées.', 'FR', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'Pour le moment, la pratique de l''apport de matériel personnel (Bring Your Own Device) dans l''environnement professionnel n''est pas possible dans l''organisme. Si cela est néanmoins amené à changer un jour, il est important de faire attention:', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Le matériel personnel ne peut pas être utilisé dans un organisme sans contrôles et explications préalables. Les explications endiguent certaines attaques, particulièrement dès lors que la distinction des dangers et des choses qui peuvent arriver est faite.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Il doit être sous un contrôle antiviral pour s''assurer d''éviter un maximum d''infection sur le réseau.', 'FR', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Cette pratique nécessite des explications pour être comprise au mieux possible.', 'FR', 'R');

-- EN
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'The company should define rules in order to avoid misapprehensions.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Rules (organisational, IT or working ones) should be known and explained to everyone, at least orally.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'If an oral transmission could be enough for a small company, rules still should be written in a charter, read and signed by everyone, more importantly if the company grows.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'An oral transmission could be a lot more complicated when there are lots of different people or work, and is really impossible when lots of people come in and out.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Besides, written rules can :
	- avoid to forget some points
	- have a legal proof if the rules have been read.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'If it''s possible, rules should be as short and as easy as possible to be attractive and readable.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Rules that are too long or too heavy with technical vocabulary could become confusing.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Each time when it''s possible, some advice or some best practices should be given, or sometime explained.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Some differences could be done depending on the role, or if it''s a temporary contract for instance.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'For the moment, the company does not have a lot of personal data, or haven''t done anything to it. If there is more personal data, or if nothing were done, the company should think:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Define, whenever it''s possible, someone should be responsible for the personal data in order to avoid the lack of response when there is an incident.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Data Lifecycle should be accessible by everyone :
	- How they are obtained
	- How they are used
	- How they are accessible, by whom and the contract linked
	- How they are alterable
	- How much time they are stored
	- How they are destroyed
This cycle should be described somewhere and accessible by anyone (sell contracts, websites, files that could be shown ...).', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'People should know who is the responsible in order to ask all the necessary questions, or the data sensibility.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'Concerning the image rights, some authorisations should be asked (to take an image and to diffuse it), and people should know when a place is under video surveillance.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Training about daily tasks is important to avoid all the basic mistakes and loss of time, and should always be updated during the lifetime to have the best practices.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Learning to use software also avoid time loss, data loss and wrong manipulation.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'By informing about attacks that are common or well-known, people could more easily guess and avoid doing anything wrong.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Some training that is done in intern does not have the same impact as external, but could be more appropriate by the mastered subject of the company environment.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Alert users on manipulated information sensibility to in order to put their attention on protections to have.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'It''s important to define responsibilities, externally or internally, with one person or more, or a company, but specialised into their own domain, if possible with training.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'For now, no outside work is done. If it''s changed, it''s important to take care of:
	- External connection which is not controlled should be avoided to avoid data loss.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Whenever users have the need to work outside, from home office to missions outside the premises, they must have a VPN connection to connect to the server.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'External connection which is not controlled should be avoided to avoid data loss.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'The visual environment is really important, to avoid curiosity or spying.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Devices that are taken away and that contains confidential data should always have their intern memory ciphered to avoid data loss.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'For now, no contracts with third parties are signed. If it''s changed, it''s important to:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'If confidential data are accessible by different third parties, it should always be under a Non-Disclosure Agreement (NDA). An IT who can access to all the data used, the cleaning staff, or a fiduciary that get financial data are only examples.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'If means and needs permit-it, a contract should be signed to ensure that the external IT manager will ensure the system to be operational on a time amount that is under the uptime needed.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'It''s necessary to review the contracts to ensure :
	- not to have solutions whenever it''s essential
	- not to pay too much for a service which is not necessary
	- to see if the services paid worth what they cost', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'For now, no third parties clean the premises. If it change, it''s important to:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'The office cleaning should be done, whenever it''s possible, during work time to ensure surveillance.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Rules should be given mainly to specify what should be done or avoided.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'If the cleaning staff is external, it''s important to define all the contracts that are bound to the confidentiality by hearing or seeing confidential data.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'Concerning the human curiosity, it is important to have a clean desk, inaccessible at first sight.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'The staff shouldn''t clean rooms that do not have any sensible equipment or data, such as archive room or IT room.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Advice should be given to avoid weak passwords. Some tips or techniques could be given to avoid frequent forget from employees. Here some examples:
	- Passwords should be kept secret and personal. Each and everyone should access their data by using their password, even from a computer of someone else.
	- There shouldn''t be a computer which is shared with one and unique password. If it''s inevitable, then a responsible should be defined, and access should be really limited.
	- It''s mandatory to be careful with the password storage in the internet browser as they are not protected.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Passwords should be kept secret and personal. If it''s impossible, then there should be a responsible for the computer to ensure its use, and give minimum access.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Passwords should be kept secret and personal. Each and everyone should access their data by using their password, even from a computer of someone else.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'It''s necessary to have passwords which had at least one uppercase, lowercase, digit and special character, for a total of 12 characters or more.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Passwords shouldn''t be a coherent word or date, except for a complete sentence.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Complete sentences could be used, even if they represent complete words.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Passwords should be changed from time to time, to ensure a leak.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'To make the storage easier, a password manager could be used.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'It''s mandatory to be careful with the password storage in the internet browser as they are not protected.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Same passwords used on different website make leak easier. Besides, only one leak is enough to compromise all the access that is the same.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'For now, wireless network isn''t activated in the company. If it is changed, it''s important to:
	- Wireless Network should be split between internal and external users to avoid access problems.
	- If a wireless network is used for external persons, some heavy protections should be taken, for example an identity collection.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Wireless Network should be split between internal and external users to avoid access problems.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'If a wireless network is used for external persons, some heavy protections should be taken, for example an identity collection.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'The password shouldn''t be easily guessable, to avoid connection which is not wanted.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Also, wireless network of printers should be protected to avoid the leak of all printed documents.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'The company should have an anti-virus and be careful to:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'An anti-virus software must be on all devices.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'It should be up to date, at least automatically to cover as many.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'It should be activated in any cases to protect the device continually.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'All devices, like smartphones, tablets should have an anti-virus, even if it''s the one by default into the operating system.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Some tests should be done from time to time.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Some tests should be done in case of suspicion of infection.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Some rules and specific advice should be given concerning users stations or laptop. Some points that are important:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'A device should always be up to date in order to avoid security problems, and also avoid network intrusion. Many operating system now make their update automatically, but software still needs some permission which should be given.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Administrator rights should be let only to the users who are specialised into IT, or well informed with advice and rules.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Downloads should be done on the official website, from the developers of the software, to avoid illegal download or infections.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Devices should be locked to avoid identity theft.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'It''s important to have backups for lots of reason, to have redundancy into data if they disappeared. It''s important to have:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Backups should concern the whole company, and everyone should be aware to put all data to ensure to have a copy of them.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Backups should be done daily to avoid major data loss.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Backups should be retained at least a month to avoid ransomware.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Backups should be outside the premises, beyond 3 kilometres.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Backups should be disconnected, outside the local network, to be invisible by cryptoransomware.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Backups should be tested from time to time, just to ensure that they are right.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Backups should be ciphered to avoid problems concerning the data theft, mainly if they are moved.', 'EN', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'For now, the personal devices are not bringing in the local network. If it''s changed, it''s important to:', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Personal devices shouldn''t be used in company without any controls or explanations. By knowing all the differences existing ways to attack an organism, it''s possible to stop some attacks, or be warned under some suspicious contacts.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Personal devices should be under antivirus control to avoid many attacks as possible.', 'EN', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Precise some rules help to protect the internal network.', 'EN', 'R');

-- DE
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC001', 'Das Unternehmen sollte Regeln definieren, um Missverständnisse zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC002', 'Regeln (organisatorische, IT- oder Arbeitsregeln) sollten zumindest mündlich bekannt sein und jedem erklärt werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC003', 'Wenn eine mündliche Übermittlung für ein kleines Unternehmen ausreichen könnte, sollten die Regeln dennoch in einer Charta festgehalten, von allen gelesen und unterzeichnet werden, was noch wichtiger ist, wenn das Unternehmen wächst.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC004', 'Eine mündliche Übermittlung könnte viel komplizierter sein, wenn es viele verschiedene Leute oder Arbeiten gibt, und ist wirklich unmöglich, wenn viele Leute rein und raus kommen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC005', 'Außerdem können schriftliche Regeln:
	- einige Punkte nicht vergessen
	- einen gesetzlichen Nachweis haben, wenn die Regeln gelesen wurden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC006', 'Wenn es möglich ist, sollten die Regeln so kurz und einfach wie möglich sein, um attraktiv und lesbar zu sein.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC007', 'Zu lange oder zu strenge Regeln mit technischem Vokabular können verwirrend werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC008', 'Jedes Mal, wenn es möglich ist, sollten einige Ratschläge oder Best Practices gegeben oder irgendwann erklärt werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q001REC009', 'Einige Unterschiede können je nach Rolle oder zum Beispiel bei einem befristeten Vertrag auftreten.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC001', 'Derzeit verfügt das Unternehmen nicht über viele personenbezogene Daten oder hat nichts dagegen unternommen. Wenn es mehr personenbezogene Daten gibt oder wenn nichts unternommen wurde, sollte das Unternehmen folgende Überlegungen anstellen:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC002', 'Definieren Sie, wann immer es möglich ist, jemanden, der für die personenbezogenen Daten verantwortlich ist, um zu vermeiden, dass bei einem Vorfall keine Reaktion erfolgt.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC003', 'Der Datenlebenszyklus sollte für alle zugänglich sein:
	- Wie sie erhalten werden
	- Wie sie verwendet werden
	- Wie sind sie zugänglich, von wem und dem Vertrag verbunden
	- Wie sie veränderbar sind
	- Wie viel Zeit sind sie gespeichert
	- Wie sie zerstört werden
Dieser Zyklus sollte irgendwo beschrieben und für jedermann zugänglich sein (Verkaufsverträge, Websites, Dateien, die angezeigt werden könnten ...).', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC004', 'Die Leute sollten wissen, wer der Verantwortliche ist, um alle notwendigen Fragen oder die Sensibilität der Daten zu stellen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q002REC005', 'In Bezug auf die Bildrechte sollten einige Autorisierungen angefordert werden (um ein Bild aufzunehmen und zu verbreiten), und die Leute sollten wissen, wann ein Ort unter Videoüberwachung steht.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC001', 'Das Training der täglichen Aufgaben ist wichtig, um alle grundlegenden Fehler und Zeitverluste zu vermeiden. Es sollte im Laufe des Lebens stets aktualisiert werden, um die besten Vorgehensweisen zu erhalten.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC002', 'Das Erlernen des Gebrauchs von Software vermeidet auch Zeitverlust, Datenverlust und falsche Manipulation.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC003', 'Durch das Informieren über häufige oder bekannte Angriffe könnten die Leute leichter erraten und vermeiden, dass etwas falsch gemacht wird.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC004', 'Einige Schulungen, die in Praktika durchgeführt werden, haben nicht die gleichen Auswirkungen wie externe, könnten jedoch für das beherrschte Thema des Unternehmensumfelds angemessener sein.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q003REC005', 'Benutzer auf manipulierte Informationen sensibilisieren, um ihre Aufmerksamkeit auf Schutzmaßnahmen zu lenken.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q004REC001', 'Es ist wichtig, die Verantwortlichkeiten extern oder intern mit einer oder mehreren Personen oder einem Unternehmen zu definieren, die jedoch, wenn möglich mit Schulungen, auf ihre eigene Domäne spezialisiert sind.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC001', 'Im Moment wird keine Außenarbeit geleistet. Wenn es geändert wird, ist es wichtig, auf Folgendes zu achten:
	- Externe Verbindungen, die nicht kontrolliert werden, sollten vermieden werden, um Datenverlust zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC002', 'Immer wenn Benutzer im Freien arbeiten müssen, vom Heimbüro bis zu Aufgaben außerhalb des Unternehmens, müssen sie über eine VPN-Verbindung verfügen, um eine Verbindung zum Server herstellen zu können.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC003', 'Externe Verbindungen, die nicht kontrolliert werden, sollten vermieden werden, um Datenverlust zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC004', 'Die visuelle Umgebung ist sehr wichtig, um Neugierde und Spionage zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q005REC005', 'Bei Geräten, die entfernt werden und vertrauliche Daten enthalten, sollte der interne Speicher immer verschlüsselt sein, um Datenverlust zu vermeiden.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC001', 'Derzeit werden keine Verträge mit Dritten abgeschlossen. Wenn es geändert wird, ist es wichtig:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC002', 'Wenn vertrauliche Daten für verschiedene Dritte zugänglich sind, sollten sie immer einer Geheimhaltungsvereinbarung (Non Disclosure Agreement, NDA) unterliegen. Eine IT, die auf alle verwendeten Daten zugreifen kann, das Reinigungspersonal oder ein Treuhänder, der Finanzdaten abruft, sind nur Beispiele.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC003', 'Wenn Mittel und Anforderungen dies zulassen, sollte ein Vertrag unterzeichnet werden, um sicherzustellen, dass der externe IT-Manager das System zu einem Zeitpunkt einsatzbereit macht, der unter der erforderlichen Betriebszeit liegt.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q006REC004', 'Es ist notwendig, die Verträge zu überprüfen, um sicherzustellen, dass:
	- keine Lösungen zu haben, wenn es notwendig ist
	- nicht zu viel für eine Dienstleistung zu bezahlen, die nicht notwendig ist
	- um zu sehen, ob die bezahlten Leistungen das wert sind, was sie kosten', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC001', 'Derzeit reinigen keine Dritten die Räumlichkeiten. Wenn es sich ändert, ist es wichtig:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC002', 'Die Büroreinigung sollte, wann immer es möglich ist, während der Arbeitszeit erfolgen, um die Überwachung zu gewährleisten.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC003', 'Regeln sollten hauptsächlich angegeben werden, um zu spezifizieren, was getan oder vermieden werden soll.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC004', 'Wenn das Reinigungspersonal extern ist, ist es wichtig, alle Verträge zu definieren, die zur Vertraulichkeit verpflichtet sind, indem vertrauliche Daten angehört oder angezeigt werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC005', 'In Bezug auf die menschliche Neugier ist es wichtig, einen auf den ersten Blick unzugänglichen, sauberen Schreibtisch zu haben.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q007REC006', 'Das Personal sollte keine Räume reinigen, in denen keine vernünftigen Geräte oder Daten vorhanden sind, z. B. Archiv- oder IT-Räume.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC001', 'Es sollten Hinweise gegeben werden, um schwache Passwörter zu vermeiden. Einige Tipps oder Techniken könnten gegeben werden, um ein häufiges Vergessen durch die Mitarbeiter zu vermeiden. Hier einige Beispiele:
	- Passwörter sollten geheim und persönlich gehalten werden. Jeder sollte mit seinem Passwort auf seine Daten zugreifen, auch von einem Computer eines anderen.
	- Es sollte keinen Computer geben, der mit einem eindeutigen Kennwort geteilt wird. Wenn es unvermeidlich ist, sollte ein Verantwortlicher definiert werden und der Zugang sollte wirklich eingeschränkt sein.
	- Beim Speichern von Passwörtern im Internetbrowser ist Vorsicht geboten, da diese nicht geschützt sind.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC002', 'Passwörter sollten geheim und persönlich gehalten werden. Wenn dies nicht möglich ist, sollte der Computer dafür verantwortlich sein, seine Verwendung sicherzustellen und einen Mindestzugriff zu gewähren.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC003', 'Passwörter sollten geheim und persönlich gehalten werden. Jeder sollte mit seinem Passwort auf seine Daten zugreifen, auch von einem Computer eines anderen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC004', 'Kennwörter mit mindestens einem Groß-, Klein-, Ziffern- und Sonderzeichen müssen mindestens 12 Zeichen lang sein.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC005', 'Passwörter sollten kein zusammenhängendes Wort oder Datum sein, mit Ausnahme eines vollständigen Satzes.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC006', 'Es können vollständige Sätze verwendet werden, auch wenn sie vollständige Wörter darstellen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC007', 'Passwörter sollten von Zeit zu Zeit geändert werden, um ein Leck zu gewährleisten.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC008', 'Um die Speicherung zu vereinfachen, könnte ein Passwort-Manager verwendet werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC009', 'Beim Speichern von Passwörtern im Internetbrowser ist Vorsicht geboten, da diese nicht geschützt sind.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q008REC010', 'Dieselben Passwörter, die auf verschiedenen Websites verwendet werden, erleichtern das Auslaufen. Außerdem ist nur ein Leck ausreichend, um den gesamten Zugriff zu gefährden, der gleich ist.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC001', 'Derzeit ist das drahtlose Netzwerk in der Firma nicht aktiviert. Wenn es geändert wird, ist es wichtig:
	- Das drahtlose Netzwerk sollte zwischen internen und externen Benutzern aufgeteilt werden, um Zugriffsprobleme zu vermeiden.
	- Wenn ein drahtloses Netzwerk für externe Personen verwendet wird, sollten einige strenge Sicherheitsvorkehrungen getroffen werden, beispielsweise eine Identitätserfassung.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC002', 'Das drahtlose Netzwerk sollte zwischen internen und externen Benutzern aufgeteilt werden, um Zugriffsprobleme zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC003', 'Wenn ein drahtloses Netzwerk für externe Personen verwendet wird, sollten einige umfassende Schutzmaßnahmen getroffen werden, z. B. eine Identitätserfassung.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC004', 'Das Passwort sollte nicht leicht zu erraten sein, um eine unerwünschte Verbindung zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q009REC005', 'Ein drahtloses Netzwerk von Druckern sollte ebenfalls geschützt werden, um das Auslaufen aller gedruckten Dokumente zu vermeiden.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC001', 'Das Unternehmen sollte über ein Virenschutzprogramm verfügen und Folgendes beachten:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC002', 'Auf allen Geräten muss eine Antivirensoftware installiert sein.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC003', 'Es sollte auf dem neuesten Stand sein, zumindest automatisch, um so viele abzudecken.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC004', 'Es sollte in jedem Fall aktiviert werden, um das Gerät dauerhaft zu schützen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC005', 'Alle Geräte, wie Smartphones und Tablets, sollten mit einem Antivirenprogramm ausgestattet sein, auch wenn dieses standardmäßig im Betriebssystem installiert ist.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC006', 'Einige Tests sollten von Zeit zu Zeit durchgeführt werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q010REC007', 'Bei Verdacht auf eine Infektion sollten einige Tests durchgeführt werden.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC001', 'Einige Regeln und spezielle Hinweise sollten in Bezug auf Benutzerstationen oder Laptops gegeben werden. Einige wichtige Punkte:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC002', 'Ein Gerät sollte immer auf dem neuesten Stand sein, um Sicherheitsprobleme und auch das Eindringen in das Netzwerk zu vermeiden. Viele Betriebssysteme führen ihre Updates jetzt automatisch durch, aber die Software benötigt noch einige Berechtigungen, die erteilt werden sollten.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC003', 'Administratorrechte sollten nur an Benutzer vergeben werden, die auf IT spezialisiert sind oder mit Ratschlägen und Regeln gut informiert sind.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC004', 'Downloads sollten von den Entwicklern der Software auf der offiziellen Website durchgeführt werden, um illegale Downloads oder Infektionen zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q011REC005', 'Geräte sollten gesperrt sein, um Identitätsdiebstahl zu vermeiden.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC001', 'Es ist aus vielen Gründen wichtig, Backups zu haben, damit die Daten redundant sind, wenn sie verschwunden sind. Es ist wichtig zu haben:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC002', 'Backups sollten das gesamte Unternehmen betreffen, und jeder sollte sich bewusst sein, alle Daten zu speichern, um sicherzustellen, dass eine Kopie davon vorliegt.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC003', 'Backups sollten täglich durchgeführt werden, um Datenverluste zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC004', 'Backups sollten mindestens einen Monat aufbewahrt werden, um Ransomware zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC005', 'Backups sollten sich außerhalb des Geländes über 3 Kilometer befinden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC006', 'Backups sollten außerhalb des lokalen Netzwerks getrennt werden, damit sie von Cryptoransomware nicht erkannt werden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC007', 'Backups sollten von Zeit zu Zeit getestet werden, um sicherzustellen, dass sie richtig sind.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q012REC008', 'Backups sollten verschlüsselt werden, um Probleme mit dem Datendiebstahl zu vermeiden, vor allem, wenn sie verschoben werden.', 'DE', 'R');

INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC001', 'Derzeit bringen die persönlichen Geräte kein lokales Netzwerk ein. Wenn es geändert wird, ist es wichtig:', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC002', 'Persönliche Geräte sollten nicht ohne Kontrollen oder Erklärungen in der Firma verwendet werden. Wenn Sie alle Unterschiede kennen, mit denen ein Organismus angegriffen werden kann, können Sie einige Angriffe stoppen oder sich bei verdächtigen Kontakten warnen lassen.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC003', 'Persönliche Geräte sollten unter Virenschutz gestellt werden, um möglichst viele Angriffe zu vermeiden.', 'DE', 'R');
INSERT INTO "survey_translationkey" ("key", "text", "lang", "ttype") VALUES ('Q013REC004', 'Präzise Regeln tragen zum Schutz des internen Netzwerks bei.', 'DE', 'R');
