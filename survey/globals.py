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
