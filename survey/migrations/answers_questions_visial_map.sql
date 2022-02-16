select qq.id a_q_id, qq.label answer_q, a.id answer_id, a.label answer_label, q.id q_id, q.label question_label, branch, "level", "order"
from survey_surveyanswerquestionmap m
    inner join survey_surveyquestion q on m.question_id = q.id
    inner join survey_surveyquestionanswer a on m.answer_id = a.id
    inner join survey_surveyquestion qq on a.question_id = qq.id
order by a.id, level, branch, "order"
