-- The sql is used to convert old labels format to the new one. --
update survey_surveyquestionservicecategory set label = 'Personal Data Processing' where label = 'SERVCAT001DATA';
update survey_surveyquestionservicecategory set label = 'Register of Processing activities' where label = 'SERVCAT002ROPA';
update survey_surveyquestionservicecategory set label = 'Transparency' where label = 'SERVCAT003TRANSS';
update survey_surveyquestionservicecategory set label = '(Some) Principles of Processing' where label = 'SERVCAT004PRINC';
update survey_surveyquestionservicecategory set label = 'Data Breaches' where label = 'SERVCAT005BRE';
update survey_surveyquestionservicecategory set label = 'Data Protection Responsible and Data Subject Rights' where label = 'SERVCAT006RIGHTS';
update survey_surveyquestionservicecategory set label = 'Management of the Risks of the Organisation' where label = 'SERVCAT007RISKS';
update survey_surveyquestionservicecategory set label = 'Information Security' where label = 'SERVCAT008INFOSEC';

update survey_surveysection set label = 'Personal Data Management' where label = 'SECTION001DATAM';
update survey_surveysection set label = 'Transparency' where label = 'SECTION002TRANS';
update survey_surveysection set label = 'Principles of processing' where label = 'SECTION003PRIN';
update survey_surveysection set label = 'Data breaches, Data rights, DPO' where label = 'SECTION004BRR';
update survey_surveysection set label = 'Risk Management' where label = 'SECTION005RISK';
update survey_surveysection set label = 'Cybersecurity' where label = 'SECTION006SEC';
