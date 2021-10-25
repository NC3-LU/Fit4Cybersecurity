from django.utils.translation import gettext_lazy

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
            "button": gettext_lazy("Your results link"),
            "title": gettext_lazy("Get the results later"),
            "text": gettext_lazy(
                "To restore the results later you can copy the provided link, create a bookmark or use the code on the main page:"
            ),
            "button_download": gettext_lazy("Download direct link"),
            "button_close": gettext_lazy("Close"),
        },
        "leave_survey": {
            "title": gettext_lazy("Would like to leave the results page?"),
            "yes": gettext_lazy("Yes"),
            "no": gettext_lazy("No"),
        },
        "download": gettext_lazy("Download"),
        "report": gettext_lazy("Summary"),
        "description": gettext_lazy(
            "This is the list of recommendations to improve the information security maturity in your company, "
            + "provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment "
            + "and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey."
        ),
        "title": gettext_lazy("final summary"),
        "result": gettext_lazy("Your results"),
        "chart": gettext_lazy("Your results chart"),
        "request_diagnostic": {
            "title": gettext_lazy("About the CASES Diagnostic"),
            "description": gettext_lazy(
                "The CASES Diagnostic is a service which analyses the company maturity in the information security "
                + "depending on company's requirements. The analyse duration can take approxymately 2 hours. A consultant from CASES will come "
                + "to your companie's premises, and ask around 30 questions concerning your information security, mostly organizational questions "
                + "and possibly some technical questions. You will receive a detailed report which will contain a maturity estimation as well as "
                + "recommendations to enhance the information security maturity."
            ),
            "service_fee": gettext_lazy(
                "The CASES Diagnostic is available for all the companies located in Luxembourg and free of charge."
            ),
            "email_subject": gettext_lazy("Request diagnostic"),
            "email_body": gettext_lazy(
                "Dear Cases Team,\n\nWe would like to request a Diagnostic CASES from you.\n\n"
                + "Here is our evaluation results identifier: {userId}\n\nHere also additional information that could be useful: \n"
                + "Lastname of the contact: \nFirstname of the contact: \nEmail address of the contact: \n"
                + "Address of the company for the Diagnostic (Luxembourg only): \nDesired language for the Diagnostic: "
            ),
        },
        "request_training": {
            "description": gettext_lazy(
                "Based on your score {score}, the CASES Diagnostic is not available for your organization at this moment. "
                + "We recommend you improve the information security maturity level by implementing the recommendations listed below. "
                + "If you need any information security training to raise awareness in your company, do not hesitate to "
            ),
            "let_us_know": gettext_lazy("let us know."),
            "email_subject": gettext_lazy("Request training offer"),
            "email_body": gettext_lazy(
                "Dear Cases Team, \n\nWe would like an information about security awareness training offer. \n\n"
                + "Here is our evaluation results identifier: {userId} \n\nHere is also the information necessary to establish the offer: \n\n"
                + "Contact details: \n- Name of the contact: \n- Email address of the contact: \n\nOrganization: \n- Company Name: \n"
                + "- Company address: \n- Postal code: \n- City: \n- VAT number (if applicable): \n\nTraining: \n- Number of participants*: \n"
                + "- Desired language(s) for the training(s): \n- Personalized topics to discuss: \n\n* For a number of people greater than 25,"
                + " the training will be done in several installments, involving a higher cost.\n"
            ),
        },
        "general_feedback": {
            "button": gettext_lazy("Your feedback"),
            "title": gettext_lazy("Please provide your feedback"),
            "button_close": gettext_lazy("Close"),
            "button_send": gettext_lazy("Send"),
            "label": gettext_lazy("Your feedback"),
            "placeholder": gettext_lazy("Please share your opinion about our tool"),
        },
    },
    "question": {
        "continue_later": {
            "button": gettext_lazy("Continue later"),
            "title": gettext_lazy("Continue the evaluation later"),
            "text": gettext_lazy(
                "To continue the evaluation process later you can copy the provided link, create a bookmark or use the code to resume later on the main page:"
            ),
            "button_download": gettext_lazy("Download direct link"),
            "button_close": gettext_lazy("Close"),
        },
        "next_button": gettext_lazy("Next"),
        "back_button": gettext_lazy("Back"),
        "cancel_button": gettext_lazy("Cancel"),
        "modify_button": gettext_lazy("Modify"),
        "description": gettext_lazy(
            "We need a little information to be able to give you useful recommendations, once the self-assessment is done."
        ),
        "question": gettext_lazy("Question"),
        "title": gettext_lazy("Let's start"),
        "leave_survey": {
            "title": gettext_lazy("Would like to leave survey?"),
            "yes": gettext_lazy("Yes"),
            "no": gettext_lazy("No"),
        },
        "select_multi_descr": gettext_lazy("Multiple answers are possible."),
        "feedback_descr1": gettext_lazy(
            "This text field should not be used to answer the question."
        ),
        "feedback_descr2": gettext_lazy(
            "Please do not provide any sensitive or confidential information refering to your identity."
        ),
    },
    "review": {
        "title": gettext_lazy("Your answers review"),
        "modify_button": gettext_lazy("Modify answers"),
        "validate_answers_button": gettext_lazy("Validate answers"),
    },
    "document": {
        "questions": gettext_lazy("Questions"),
    },
    "form": {
        "error_messages": {
            "answer": {
                "required": gettext_lazy("You need to choose at least one answer"),
                "unique": gettext_lazy(
                    'You can\'t choose multiple answers if the answer "%(value)s" is choosen'
                ),
            },
        },
        "start_form": {
            "sector_question": gettext_lazy("What is your sector?"),
            "sector_list": {
                "BANK": gettext_lazy("Banking, insurance and real estate"),
                "SALE": gettext_lazy("Trading, sales and mass distribution"),
                "MARK": gettext_lazy("Marketing, media and multimedia"),
                "BUIL": gettext_lazy("Construction industries and civil engineering"),
                "REST": gettext_lazy(
                    "Hotel and restoration, tourism and entertainment"
                ),
                "INDU": gettext_lazy("Industry"),
                "INST": gettext_lazy("Installation and maintenance"),
                "ARTI": gettext_lazy(
                    "Creation or placing of objects that are artistic and decorative"
                ),
                "HEAL": gettext_lazy("Health"),
                "SERV": gettext_lazy("Home-Care Service or Community Service"),
                "SHOW": gettext_lazy("Shows"),
                "SUPP": gettext_lazy("Company Support"),
                "LOGI": gettext_lazy("Transport and Logistics"),
                "FARM": gettext_lazy(
                    "Farming and fishing, natural spaces and green spaces, animal care"
                ),
                "PUBL": gettext_lazy("Public administration"),
            },
            "size_question": gettext_lazy("How many employees?"),
            "country": {
                "label": gettext_lazy("Please select your country"),
                "required_error_message": gettext_lazy("Please select your country"),
            },
        },
        "questions": {
            "feedback_label": gettext_lazy("Your feedback"),
            "feedback_placeholder": gettext_lazy(
                "Please let us know if anything is missing"
            ),
            "custom_response": gettext_lazy("Custom response"),
        },
    },
}
