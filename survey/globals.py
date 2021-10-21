from django.utils.translation import gettext

SECTOR_CHOICES = [
    ("BANK", "Banking, insurance and real estate"),
    ("SALE", "Trading, sales and mass distribution"),
    ("MARK", "Marketing, media and multimedia"),
    ("BUIL", "Construction industries and civil engineering"),
    ("REST", "Hotel and restoration, tourism and entertainment"),
    ("INDU", "Industry"),
    ("INST", "Installation and maintenance"),
    ("ARTI", "Creation or placing of objects that are artistic and decorative"),
    ("HEAL", "Health"),
    ("SERV", "Home-Care Service or Community Service"),
    ("SHOW", "Shows"),
    ("SUPP", "Company Support"),
    ("LOGI", "Transport and Logistics"),
    ("FARM", "Farming and fishing, natural spaces and green spaces, animal care"),
    ("PUBL", "Public administration"),
]

COUNTRIES = [
    ("LU", "Luxembourg"),
    ("EEA", "EEA"),
    ("NEEA", "Not EEA"),
    ("EU", "Europe"),
]

SERVICE_TARGETS = [
    ("SME", "Small to Medium Size Entreprises"),
    ("BC", "Big Company"),
    ("MN", "Multinationals Coorporations"),
    ("IND", "Independent"),
    ("PRI", "Private Person"),
]

COMPANY_SIZE = [
    ("a", "1-5"),
    ("b", "6-10"),
    ("c", "10-20"),
    ("d", "20-50"),
    ("e", "50-100"),
    ("f", "100-200"),
    ("g", "200-500"),
    ("h", "500-1000"),
    ("i", "1000-5000"),
    ("j", "5000+"),
]

QUESTION_TYPES = [
    ("M", "Multiple Choice"),
    ("S", "Single Choice"),
    ("T", "Free text"),
    ("MT", "Multiple Choice + Free Text"),
    ("ST", "Single Choice + Free Text"),
]

ANSWER_TYPES = [
    ("P", "Predefined answer"),
    ("T", "Free text"),
]

LANG_SELECT = [
    ("en", "English"),
    ("fr", "Français"),
    ("de", "Deutsch"),
]

TRANSLATION_TYPES = [
    ("Q", "Question"),
    ("A", "Answer"),
    ("R", "Recommendation"),
    ("S", "Question Section"),
    ("C", "Company Service Category"),
]

MIN_ACCEPTABLE_SCORE = 65

TRANSLATION_UI = {
    "report": {
        "continue_later": {
            "button": gettext("Your results link"),
            "title": gettext("Get the results later"),
            "text": gettext(
                "To restore the results later you can copy the provided link, create a bookmark or use the code on the main page:"
            ),
            "button_download": gettext("Download direct link"),
            "button_close": gettext("Close"),
        },
        "leave_survey": {
            "title": gettext("Would like to leave the results page?"),
            "yes": gettext("Yes"),
            "no": gettext("No"),
        },
        "download": gettext("Download"),
        "report": gettext("Summary"),
        "description": gettext(
            "This is the list of recommendations to improve the information security maturity in your company, "
            + "provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment "
            + "and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey."
        ),
        "title": gettext("final summary"),
        "result": gettext("Your results"),
        "chart": gettext("Your results chart"),
        "request_diagnostic": {
            "title": gettext("About the CASES Diagnostic"),
            "description": gettext(
                "The CASES Diagnostic is a service which analyses the company maturity in the information security "
                + "depending on company's requirements. The analyse duration can take approxymately 2 hours. A consultant from CASES will come "
                + "to your companie's premises, and ask around 30 questions concerning your information security, mostly organizational questions "
                + "and possibly some technical questions. You will receive a detailed report which will contain a maturity estimation as well as "
                + "recommendations to enhance the information security maturity."
            ),
            "service_fee": gettext(
                "The CASES Diagnostic is available for all the companies located in Luxembourg and free of charge."
            ),
            "email_subject": gettext("Request diagnostic"),
            "email_body": gettext(
                "Dear Cases Team,\n\nWe would like to request a Diagnostic CASES from you.\n\n"
                + "Here is our evaluation results identifier: {userId}\n\nHere also additional information that could be useful: \n"
                + "Lastname of the contact: \nFirstname of the contact: \nEmail address of the contact: \n"
                + "Address of the company for the Diagnostic (Luxembourg only): \nDesired language for the Diagnostic: "
            ),
        },
        "request_training": {
            "description": gettext(
                "Based on your score {score}, the CASES Diagnostic is not available for your organization at this moment. "
                + "We recommend you improve the information security maturity level by implementing the recommendations listed below. "
                + "If you need any information security training to raise awareness in your company, do not hesitate to "
            ),
            "let_us_know": gettext("let us know."),
            "email_subject": gettext("Request training offer"),
            "email_body": gettext(
                "Dear Cases Team, \n\nWe would like an information about security awareness training offer. \n\n"
                + "Here is our evaluation results identifier: {userId} \n\nHere is also the information necessary to establish the offer: \n\n"
                + "Contact details: \n- Name of the contact: \n- Email address of the contact: \n\nOrganization: \n- Company Name: \n"
                + "- Company address: \n- Postal code: \n- City: \n- VAT number (if applicable): \n\nTraining: \n- Number of participants*: \n"
                + "- Desired language(s) for the training(s): \n- Personalized topics to discuss: \n\n* For a number of people greater than 25,"
                + " the training will be done in several installments, involving a higher cost.\n"
            ),
        },
        "general_feedback": {
            "button": gettext("Your feedback"),
            "title": gettext("Please provide your feedback"),
            "button_close": gettext("Close"),
            "button_send": gettext("Send"),
            "label": gettext("Your feedback"),
            "placeholder": gettext("Please share your opinion about our tool"),
        },
    },
    "question": {
        "continue_later": {
            "button": gettext("Continue later"),
            "title": gettext("Continue the evaluation later"),
            "text": gettext(
                "To continue the evaluation process later you can copy the provided link, create a bookmark or use the code to resume later on the main page:"
            ),
            "button_download": gettext("Download direct link"),
            "button_close": gettext("Close"),
        },
        "next_button": gettext("Next"),
        "back_button": gettext("Back"),
        "cancel_button": gettext("Cancel"),
        "modify_button": gettext("Modify"),
        "description": gettext(
            "We need a little information to be able to give you useful recommendations, once the self-assessment is done."
        ),
        "question": gettext("Question"),
        "title": gettext("Let's start"),
        "leave_survey": {
            "title": gettext("Would like to leave survey?"),
            "yes": gettext("Yes"),
            "no": gettext("No"),
        },
        "select_multi_descr": gettext("Multiple answers are possible."),
        "feedback_descr1": gettext(
            "This text field should not be used to answer the question."
        ),
        "feedback_descr2": gettext(
            "Please do not provide any sensitive or confidential information refering to your identity."
        ),
    },
    "review": {
        "title": gettext("Your answers review"),
        "modify_button": gettext("Modify answers"),
        "validate_answers_button": gettext("Validate answers"),
    },
    "document": {
        "questions": gettext("Questions"),
    },
    "form": {
        "error_messages": {
            "answer": {
                "required": gettext("You need to choose at least one answer"),
                "unique": gettext(
                    'You can\'t choose multiple answers if the answer "%(value)s" is choosen'
                ),
            },
        },
        "start_form": {
            "sector_question": gettext("What is your sector?"),
            "sector_list": {
                "BANK": gettext("Banking, insurance and real estate"),
                "SALE": gettext("Trading, sales and mass distribution"),
                "MARK": gettext("Marketing, media and multimedia"),
                "BUIL": gettext("Construction industries and civil engineering"),
                "REST": gettext("Hotel and restoration, tourism and entertainment"),
                "INDU": gettext("Industry"),
                "INST": gettext("Installation and maintenance"),
                "ARTI": gettext(
                    "Creation or placing of objects that are artistic and decorative"
                ),
                "HEAL": gettext("Health"),
                "SERV": gettext("Home-Care Service or Community Service"),
                "SHOW": gettext("Shows"),
                "SUPP": gettext("Company Support"),
                "LOGI": gettext("Transport and Logistics"),
                "FARM": gettext(
                    "Farming and fishing, natural spaces and green spaces, animal care"
                ),
                "PUBL": gettext("Public administration"),
            },
            "size_question": gettext("How many employees?"),
            "country": {
                "label": gettext("Please select your country"),
                "required_error_message": gettext("Please select your country"),
            },
        },
        "questions": {
            "feedback_label": gettext("Your feedback"),
            "feedback_placeholder": gettext(
                "Please let us know if anything is missing"
            ),
            "custom_response": gettext("Custom response"),
        },
    },
}
