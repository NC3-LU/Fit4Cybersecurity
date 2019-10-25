SECTOR_CHOICES = [
    ("gov", "Government"),
    ("adm", "Public Administrations"),
    ("fin", "Financial Sector"),
    ("it", "Information Technology (IT)"),
]

COUNTRIES = [
    ("LU", "Luxembourg"),
    ("DE", "Deutschland"),
    ("BE", "Belgique"),
    ("FR", "France"),
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
    ("I", "Integer Slider"),
]

LANG_SELECT = [
    ("EN", "English"),
    ("FR", "Français"),
    ("DE", "Deutsch"),
]

TRANSLATION_TYPES = [
    ("Q", " Question"),
    ("A", "Answer"),
    ("R", "Recommendation"),
    ("S", "Question Section"),
    ("C", "Company Service Category"),
]

MIN_ACCEPTABLE_SCORE = 80

TRANSLATION_UI = {
    'report': {
        'continue_later': {
            'button': {
                'en': "restore results",
                'fr': "restaurer les résultats",
                'de': "ergebnisse wiederherstellen",
            },
            'title': {
                'en': "Get the results later",
                'fr': "Obtenez les résultats plus tard",
                'de': "Die Ergebnisse erhalten Sie später",
            },
            'text': {
                'en': "To restore the results later you can copy the provided link, create a bookmark or use the code on the main page:",
                'fr': "Pour restaurer les résultats ultérieurement, vous pouvez copier le lien fourni, créer un signet ou utilisez le code sur la page principale:",
                'de': "Um die Ergebnisse später wiederherzustellen, können Sie den bereitgestellten Link kopieren und ein Lesezeichen erstellen oder verwenden Sie den Code auf der Hauptseite",
            },
            'button_download': {
                'en': "Download direct link",
                'fr': "Télécharger le lien direct",
                'de': "Direkten Link herunterladen",
            },
            'button_close': {
                'en': "Close",
                'fr': "Fermer",
                'de': "Schließen",
            },
        },
        'leave_survey': {
            'title': {
                'en': "Would like to leave the results page?",
                'fr': "Voulez vous quitter la page de résultats?",
                'de': "Möchten Sie die Ergebnisseite verlassen?",
            },
            'yes': {
                'en': "Yes",
                'fr': "Oui",
                'de': "Ya",
            },
            'no': {
                'en': "No",
                'fr': "Non",
                'de': "Nein",
            },
        },
        'download': {
            'en': "Download",
            'fr': "Téléchargement",
            'de': "Herunterladen",
        },
        'report': {
            'en': "Summary",
            'fr': "Résumé",
            'de': "Zusammenfassung",
        },
        'description': {
            'en': "This is the list of recommendations to improve the information security maturity in your company, provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey.",
            'fr': "Voici la liste des recommandations visant à améliorer la maturité de la sécurité de l'information dans votre entreprise, à condition que vos réponses reflètent correctement l'état de votre entreprise. N'oubliez pas non plus qu'il s'agit d'une auto-évaluation et qu'elle ne fait qu'effleurer le niveau de maturité de la sécurité de l'information. Par conséquent, nous ne sommes pas responsables des résultats de cette enquête.",
            'de': "Dies ist die Liste der Empfehlungen zur Verbesserung der Informationssicherheitsreife in Ihrem Unternehmen, sofern Ihre Antworten den Status in Ihrem Unternehmen korrekt widerspiegeln. Denken Sie auch daran, dass es sich um eine Selbsteinschätzung handelt, die nur die Oberfläche des Reifegrads der Informationssicherheit abbilden kann, und wir daher nicht für die Ergebnisse dieser Umfrage haften.",
        },
        'title': {
            'en': "final summary",
            'fr': "résumé final",
            'de': "Zusammenfassung",
        },
        'result': {
            'en': "Current",
            'fr': "Maintenant",
            'de': "Jetzt",
        },
        'resultMax': {
            'en': "Target",
            'fr': "But",
            'de': "Ziel",
        },
        'chart': {
            'en': "Your results chart",
            'fr': "Votre tableau de résultats",
            'de': "Ihr Ergebnisdiagramm",
        },
        'request_diagnostic': {
            'title': {
                'en': "About the CASES Diagnostic",
                'fr': "À propos du Diagnostic CASES",
                'de': "About the CASES Diagnostic",
            },
            'description': {
                'en': "The CASES Diagnostic is a service which analyses the company maturity in the information security depending on company's requirements. The analyse duration can take approxymately 2 hours. A consultant from CASES will come to your companie's premises, and ask around 30 questions concerning your information security, mostly organizational questions and possibly some technical questions. You will receive a detailed report which will contain a maturity estimation as well as recommendations to enhance the information security maturity.",
                'fr': "Le diagnostic CASES est un service destiné à l'analyse de la maturité d'une entreprise face à la sécurité de l'information qui lui est nécessaire. Avec une durée d'environ 2 heures, un consultant CASES se déplace dans les locaux de l'entreprise, et pose une trentaine de questions pouvant être sur le côté organisationnel aussi bien que le côté un peu plus technique. À l'issue de ce diagnostic, un rapport est envoyé, et il contiendra une estimation de la maturité ainsi que des recommandations pour améliorer la maturité en la sécurité de l'information.",
                'de': "Der Diagnostic CASES ist ein Service zur Analyse des Reifegrads eines Unternehmens im Hinblick auf die Sicherheit der benötigten Informationen. Mit einer Dauer von ungefähr 2 Stunden kommt ein CASES-Berater zu Ihnen auf ihr Firmengelände und stellt ungefähr 30 Fragen, die sowohl organisatorischer als auch etwas technischer Natur sein können. Am Ende dieses Diagnostic wird ein Bericht verfasst und Ihnen kurze Zeit später übermittelt: er enthält eine Schätzung der Laufzeit sowie Empfehlungen zur Verbesserung der Laufzeit der Informationssicherheit.",
            },
            'service_fee': {
                'en': "The CASES Diagnostic is free of charge and possible for all the companies located in Luxembourg.",
                'fr': "Le Diagnostic est gratuit et possible pour toute entreprise ayant des locaux au Luxembourg.",
                'de': "Der Diagnostic ist für jedes Unternehmen mit Sitz in Luxemburg möglich und kostenlos.",
            },
            'email_subject': {
                'en': "Request diagnostic",
                'fr': "Demander un diagnostic",
                'de': "Diagnose anfordern",
            },
            'email_body': {
                'en': "Dear Cases Team,\n\nWe would like to request a Diagnostic CASES from you.\n\nHere is our evaluation results identifier: {userId}\n\nHere also additional information that could be useful: \nLastname of the contact: \nFirstname of the contact: \nEmail address of the contact: \nAddress of the company and for the Diagnostic (Luxembourg only): \nDesired language for the Diagnostic: ",
                'fr': "À l'attention de l'équipe CASES,\n\nNous aimerions planifier un Diagnostic CASES.\n\nVoici l'identifiant lié à notre évaluation: {userId}\n\nVoici également les informations qui vous seront nécessaires: \nNom du point de contact: \nPrénom du point de contact: \nAdresse mail du point de contact: \nAdresse de l'entreprise et du Diagnostic (Luxembourg uniquement): \nLangue souhaitée du Diagnostic: ",
                'de': "Sehr geehrtes CASES Team, \n\nWir möchten ein Diagnostic CASES mit Ihnen anfordern. \n\nHier finden Sie die ID unserer Bewertungsergebnisse: {userId} \n\nHier finden Sie auch andere nützliche Informationen: \nNachname des Kontakts: \nVorname des Kontakts: \nE-Mail-Adresse des Kontakts: \nAdresse des Unternehmens und des Ortes für den Diagnostic CASES: (nur in Luxemburg): \nGewünschte Sprache für den Diagnostic CASES:",
            },
        },
    },
    'question': {
        'continue_later': {
            'button': {
                'en': "Continue later",
                'fr': "Continuer plus tard",
                'de': "Später weitermachen",
            },
            'title': {
                'en': "Continue the evaluation later",
                'fr': "Continuer l'évaluation plus tard",
                'de': "Setzen Sie die Auswertung später fort",
            },
            'text': {
                'en': "To continue the evaluation process later you can copy the provided link, create a bookmark or use the code to resume later on the main page:",
                'fr': "Pour continuer le processus d’évaluation plus tard, vous pouvez copier le lien fourni, créer un signet ou utiliser le code pour reprendre plus tard sur la page principale:",
                'de': "Um den Evaluierungsprozess später fortzusetzen, können Sie den bereitgestellten Link kopieren und ein Lesezeichen erstellen oder verwenden Sie den Code, um später auf der Hauptseite fortzufahren:",
            },
            'button_download': {
                'en': "Download direct link",
                'fr': "Télécharger le lien direct",
                'de': "Direkten Link herunterladen",
            },
            'button_close': {
                'en': "Close",
                'fr': "Fermer",
                'de': "Schließen",
            },
        },
        'next_button': {
            'en': "Next",
            'fr': "Suite",
            'de': "Nächster",
        },
        'description': {
            'en': "Before we start, we need a little information to be able to give you useful recommendations, once the self-assessment is done.",
            'fr': "Avant de commencer, nous avons besoin de quelques informations pour pouvoir vous faire des recommandations utiles, une fois l’auto-évaluation terminée.",
            'de': "Bevor wir beginnen, benötigen wir einige Informationen, um Ihnen nützliche Empfehlungen geben zu können, sobald die Selbsteinschätzung abgeschlossen ist.",
        },
        'question': {
            'en': "Question",
            'fr': "Question",
            'de': "Frage",
        },
        'title': {
            'en': "Let's start",
            'fr': "Commençons",
            'de': "Lasst uns beginnen",
        },
        'leave_survey': {
            'title': {
                'en': "Would like to leave survey?",
                'fr': "Voulez vous quitter l'enquête?",
                'de': "Möchten Sie die Umfrage verlassen?",
            },
            'yes': {
                'en': "Yes",
                'fr': "Oui",
                'de': "Ya",
            },
            'no': {
                'en': "No",
                'fr': "Non",
                'de': "Nein",
            },
        },
    },
    'document': {
        'questions': {
            'en': "Questions",
            'fr': "Questions",
            'de': "Fragen",
        },
    },
    'form': {
        'error_messages': {
            'answer': {
                'required': {
                    'en': "You need to choose at least one answer",
                    'fr': "Vous devez choisir au moins une réponse",
                    'de': "Sie müssen mindestens eine Antwort auswählen",
                },
                'unique': {
                    'en': "You can't choose multiple answers if the answer \"%(value)s\" is choosen",
                    'fr': "Vous ne pouvez pas choisir plusieurs réponses si la réponse \"%(value)s\" est choisie",
                    'de': "Sie können nicht mehrere Antworten auswählen, wenn die Antwort \"%(value)s\" ausgewählt ist",
                },
            },
        },
        'start_form': {
            'sector_question': {
                'en': "What is your sector?",
                'fr': "Quel est votre secteur?",
                'de': "Was ist Ihre Branche?",
            },
            'sector_list': {
                'gov': {
                    'en': "Government",
                    'fr': "Gouvernement",
                    'de': "Regierung",
                },
                'adm': {
                    'en': "Public Administrations",
                    'fr': "Administrations publiques",
                    'de': "Öffentliche Verwaltungen",
                },
                'fin': {
                    'en': "Financial Sector",
                    'fr': "Secteur financier",
                    'de': "Finanzsektor",
                },
                'it': {
                    'en': "Information Technology (IT)",
                    'fr': "Information Technologique (IT)",
                    'de': "Informationstechnologie (IT)",
                },
            },
            'size_question': {
                'en': "How many employees?",
                'fr': "Combien d'employés?",
                'de': "Wie viele mitarbeiter?",
            },
        },
    },
}
