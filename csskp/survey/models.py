from django.db import models

# Create your models here.

# REMEMBER: use models.UUIDField for every object

class SurveySection:
    # Section ID
    pass

class SurveyQuestion:
    # Question id --> translation in other table
    # QuestionCatID
    # Section ID
    pass

class SurveyQuestionAnswer:
    # Answer id --> translation in other table
    # Question id --> can be 1-question to multi-answers
    pass

class SurveyUser:
    # user ID - Hash or UUID
    # Sector
    # OtherSector Description
    # number of employees
    pass

class SurveyUserAnswers:
    # UUID user
    # QuestionID
    # AnswerListID
    pass

class SurveyUserAnswer:
    # AnswerID
    # AnswerListID
    pass

class SurveyQuestionServiceCategory:
    # QuestionCatID
    pass