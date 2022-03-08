-- 1. We need to first create a copy of the DB fit4contract_old or export and import. One of the following:
-- CREATE DATABASE fit4contract_old WITH TEMPLATE fit4contract;
-- psql -h 127.0.0.1 -p 5434 fit4contract_old postgres < ~/web/tmp/fit4contract.pgsql

-- 2. Execute the data migrations to the new tables format.

CREATE EXTENSION IF NOT EXISTS dblink;

insert into survey_surveyquestionservicecategory select * from dblink('dbname=fit4contract_old', 'select sc.id, tr.text as label from survey_surveyquestionservicecategory as sc inner join survey_translationkey as tr on sc."titleKey" = tr.key and tr.lang = ''en''') AS t1(id int, label text);
SELECT setval('survey_surveyquestionservicecategory_id_seq', COALESCE((select max(id) from survey_surveyquestionservicecategory)::bigint, 1));

insert into survey_surveysection select * from dblink('dbname=fit4contract_old', 'select s.id, tr.text as label from survey_surveysection as s inner join survey_translationkey as tr on s."sectionTitleKey" = tr.key and tr.lang = ''en''') AS t1(id int, label text);
SELECT setval('survey_surveysection_id_seq', COALESCE((select max(id) from survey_surveysection)::bigint, 1));

insert into survey_surveyquestion select * from dblink('dbname=fit4contract_old', 'select q.qindex AS id, tr.text as label, q.qtype, q.qindex, q.section_id, q.service_category_id, q."maxPoints", ''aindex'' answers_order, true is_active, '''' tooltip from survey_surveyquestion as q inner join survey_translationkey as tr on q."titleKey" = tr.key and tr.lang = ''en'' order by q.qindex') AS t1(id int, label text, qtype text, qindex int, section_id int, service_category_id int, "maxPoints" int, answers_order text, is_active boolean, tooltip text);
SELECT setval('survey_surveyquestion_id_seq', COALESCE((select max(id) from survey_surveyquestion)::bigint, 1));

insert into survey_surveyquestionanswer select * from dblink('dbname=fit4contract_old', 'select qa.id, tr.text as label, qa.aindex / 10, q.qindex as question_id, qa."uniqueAnswer", qa.score, ''p'' as atype, 0 bonus_points, '''' value, true is_active, '''' tooltip from survey_surveyquestionanswer as qa inner join survey_translationkey as tr on qa."answerKey" = tr.key and tr.lang = ''en'' inner join survey_surveyquestion as q on q.uuid = qa.question_id') AS t1(id int, label text, aindex int, question_id int, "uniqueAnswer" boolean, score int, atype text, bonus_points int, "value" text, is_active boolean, tooltip text);
SELECT setval('survey_surveyquestionanswer_id_seq', COALESCE((select max(id) from survey_surveyquestionanswer)::bigint, 1));

insert into survey_surveyuser select * from dblink('dbname=fit4contract_old', 'select u.id, user_id, sector, e_count, status, created_at, updated_at, country_code, u.choosen_lang as chosen_lang, q.qindex as current_question_id from survey_surveyuser as u inner join survey_surveyquestion as q on q.uuid = u.current_question_id') AS t1(id int, user_id uuid, sector text, e_count text, status int, created_at date, updated_at date, country_code text, chosen_lang text, current_question_id int);
SELECT setval('survey_surveyuser_id_seq', COALESCE((select max(id) from survey_surveyuser)::bigint, 1));

insert into survey_surveyuseranswer select * from dblink('dbname=fit4contract_old', 'select id, uvalue, answer_id, user_id, '''' content from survey_surveyuseranswer') AS t1(id int, uvalue text, answer_id int, user_id int, content text);
SELECT setval('survey_surveyuseranswer_id_seq', COALESCE((select max(id) from survey_surveyuseranswer)::bigint, 1));

insert into survey_surveyuserfeedback select * from dblink('dbname=fit4contract_old', 'select f.id, feedback, q.qindex as question_id, f.user_id from survey_surveyuserfeedback as f inner join survey_surveyquestion as q on q.uuid = f.question_id') AS t1(id int, feedback text, question_id int, user_id int);
SELECT setval('survey_surveyuserfeedback_id_seq', COALESCE((select max(id) from survey_surveyuserfeedback)::bigint, 1));

insert into survey_recommendations select * from dblink('dbname=fit4contract_old', 'select r.id, tr.text as label, min_e_count, max_e_count, sector, "answerChosen", "forAnswer_id" from survey_recommendations as r inner join survey_translationkey as tr on r."textKey" = tr.key and tr.lang = ''en''') AS t1(id int, label text, min_e_count text, max_e_count text, sector text, "answerChosen" boolean, "forAnswer_id" int);
SELECT setval('survey_recommendations_id_seq', COALESCE((select max(id) from survey_recommendations)::bigint, 1));

insert into survey_recommendations_categories (recommendations_id, surveyquestionservicecategory_id) select * from dblink('dbname=fit4contract_old', 'select r.id as recommendation_id, service_category_id from survey_recommendationcategory as rc inner join survey_recommendations as r on r."textKey" = rc.recommendation_key order by r.id') AS t1(recommendation_id int, service_category_id int);

insert into survey_surveyuserquestionsequence select * from dblink('dbname=fit4contract_old', 'select s.id, s.branch, s.level, s.index, has_been_answered, s.is_active, q.qindex as question_id, s.user_id from survey_surveyuserquestionsequence as s inner join survey_surveyquestion as q on q.uuid = s.question_id') AS t1(id int, branch int, "level" int, "index" int, has_been_answered boolean, is_active boolean, question_id int, user_id int);
SELECT setval('survey_surveyuserquestionsequence_id_seq', COALESCE((select max(id) from survey_surveyuserquestionsequence)::bigint, 1));

insert into survey_surveyanswerquestionmap select * from dblink('dbname=fit4contract_old', 'select aqm.id, branch, level, "order", aqm.answer_id, q.qindex as question_id from survey_surveyanswerquestionmap as aqm inner join survey_surveyquestion as q on q.uuid = aqm.question_id') AS t1(id int, branch int, "level" int, "order" int, answer_id int, question_id int);
SELECT setval('survey_surveyanswerquestionmap_id_seq', COALESCE((select max(id) from survey_surveyanswerquestionmap)::bigint, 1));

-- 3. Execute the context questions import command.

-- 4. Recreate all the context questions answers.
-- execute the command insertcontextanswers with the data from fit4contract_users_data.json

-- 5. Drop the 3 fields from survey_surveyuser
ALTER TABLE survey_surveyuser
DROP COLUMN IF EXISTS sector,
DROP COLUMN IF EXISTS e_count,
DROP COLUMN IF EXISTS country_code;
