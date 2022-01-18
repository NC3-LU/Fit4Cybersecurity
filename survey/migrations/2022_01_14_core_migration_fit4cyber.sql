-- The sql is used to convert old labels format to the new one. --
update survey_surveyquestionservicecategory set label = "Passwords" where label = "SERVCAT001PWDS"
update survey_surveyquestionservicecategory set label = "Contracts (SLA/NDA)" where label = "SERVCAT002SNDA"
update survey_surveyquestionservicecategory set label = "WiFi" where label = "SERVCAT003WIFI"
update survey_surveyquestionservicecategory set label = "Rules/Charter" where label = "SERVCAT004RCHA"
update survey_surveyquestionservicecategory set label = "Trainings" where label = "SERVCAT005TRAI"
update survey_surveyquestionservicecategory set label = "Backups" where label = "SERVCAT006BACK"
update survey_surveyquestionservicecategory set label = "GDPR" where label = "SERVCAT007GDPR"
update survey_surveyquestionservicecategory set label = "BYOD" where label = "SERVCAT008BYOD"
update survey_surveyquestionservicecategory set label = "Home Office/Mobility" where label = "SERVCAT009TELE"
update survey_surveyquestionservicecategory set label = "User Work Stations/Updates" where label = "SERVCAT010UPDT"
update survey_surveyquestionservicecategory set label = "Antivirus" where label = "SERVCAT011AVIR"
update survey_surveyquestionservicecategory set label = "IT and Information Security Responsibilities" where label = "SERVCAT012REIT"
update survey_surveyquestionservicecategory set label = "Office Cleaning" where label = "SERVCAT013CLEA"

update survey_surveysection set label = "Awareness and Compliance" where label = "SECTION001OC"
update survey_surveysection set label = "Employee Management" where label = "SECTION002GE"
update survey_surveysection set label = "Third Party Management" where label = "SECTION003GT"
update survey_surveysection set label = "Logical Access" where label = "SECTION004AL"
update survey_surveysection set label = "Local Area Network" where label = "SECTION005RI"
update survey_surveysection set label = "Information System" where label = "SECTION006IT"