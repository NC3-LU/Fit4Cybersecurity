SECTOR_CHOICES = [
    ("BANK", "Banking"),
    ("FINA", "Central Bank"),
    ("MIFI", "Micro-Finance"),
    ("MIAS", "Micro Assurance"),
    ("MOMO", "Mobile Money"),
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
    ("MINE", "Oil & Gas"),
    ("OTMI", "Other Mines"),
]

COUNTRIES = [
    ("SN", "Senegal"),
    ("RW", "Rwanda"),
    ("CI", "Ivory Coast"),
    ("NG", "Nigeria"),
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
            "button": {
                "en": "Your results link",
                "fr": "Votre lien de résultats",
                "de": "Ihr Ergebnislink",
            },
            "title": {
                "en": "Get the results later",
                "fr": "Obtenez les résultats plus tard",
                "de": "Die Ergebnisse erhalten Sie später",
            },
            "text": {
                "en": "To restore the results later you can copy the provided link, create a bookmark or use the code on the main page:",
                "fr": "Pour restaurer les résultats ultérieurement, vous pouvez copier le lien fourni, créer un signet ou utilisez le code sur la page principale:",
                "de": "Um die Ergebnisse später wiederherzustellen, können Sie den bereitgestellten Link kopieren und ein Lesezeichen erstellen oder verwenden Sie den Code auf der Hauptseite",
            },
            "button_download": {
                "en": "Download direct link",
                "fr": "Télécharger le lien direct",
                "de": "Direkten Link herunterladen",
            },
            "button_close": {
                "en": "Close",
                "fr": "Fermer",
                "de": "Schließen",
            },
        },
        "leave_survey": {
            "title": {
                "en": "Would like to leave the results page?",
                "fr": "Voulez vous quitter la page de résultats?",
                "de": "Möchten Sie die Ergebnisseite verlassen?",
            },
            "yes": {
                "en": "Yes",
                "fr": "Oui",
                "de": "Ja",
            },
            "no": {
                "en": "No",
                "fr": "Non",
                "de": "Nein",
            },
        },
        "download": {
            "en": "Download",
            "fr": "Téléchargement",
            "de": "Herunterladen",
        },
        "report": {
            "en": "Summary",
            "fr": "Résumé",
            "de": "Zusammenfassung",
        },
        "description": {
            "en": "This is the list of recommendations to improve the information security maturity in your company, provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey.",
            "fr": "Voici la liste des recommandations visant à améliorer la maturité de la sécurité de l'information dans votre entreprise, à condition que vos réponses reflètent correctement l'état de votre entreprise. N'oubliez pas non plus qu'il s'agit d'une auto-évaluation et qu'elle ne fait qu'effleurer le niveau de maturité de la sécurité de l'information. Par conséquent, nous ne sommes pas responsables des résultats de cette enquête.",
            "de": "Dies ist die Liste der Empfehlungen zur Verbesserung der Informationssicherheitsreife in Ihrem Unternehmen, sofern Ihre Antworten den Status in Ihrem Unternehmen korrekt widerspiegeln. Denken Sie auch daran, dass es sich um eine Selbsteinschätzung handelt, die nur die Oberfläche des Reifegrads der Informationssicherheit abbilden kann, und wir daher nicht für die Ergebnisse dieser Umfrage haften.",
        },
        "title": {
            "en": "final summary",
            "fr": "résumé final",
            "de": "Zusammenfassung",
        },
        "result": {
            "en": "Your results",
            "fr": "Vos résultats",
            "de": "Ihre Ergebnisse",
        },
        "chart": {
            "en": "Your results chart",
            "fr": "Votre tableau de résultats",
            "de": "Ihr Ergebnisdiagramm",
        },
        "request_diagnostic": {
            "title": {
                "en": "About the ACRC Diagnostic",
                "fr": "À propos du Diagnostic ACRC",
                "de": "About the ACRC Diagnostic",
            },
            "description": {
                "en": "The ACRC Diagnostic is a service which analyses the company maturity in the information security depending on company's requirements. The analyse duration can take approxymately 2 hours. A consultant from ACRC will come to your companie's premises, and ask around 30 questions concerning your information security, mostly organizational questions and possibly some technical questions. You will receive a detailed report which will contain a maturity estimation as well as recommendations to enhance the information security maturity.",
                "fr": "Le diagnostic ACRC est un service destiné à l'analyse de la maturité d'une entreprise face à la sécurité de l'information qui lui est nécessaire. Avec une durée d'environ 2 heures, un consultant ACRC se déplace dans les locaux de l'entreprise, et pose une trentaine de questions pouvant être sur le côté organisationnel aussi bien que le côté un peu plus technique. À l'issue de ce diagnostic, un rapport est envoyé, et il contiendra une estimation de la maturité ainsi que des recommandations pour améliorer la maturité en la sécurité de l'information.",
                "de": "Der Diagnostic ACRC ist ein Service zur Analyse des Reifegrads eines Unternehmens im Hinblick auf die Sicherheit der benötigten Informationen. Mit einer Dauer von ungefähr 2 Stunden kommt ein ACRC-Berater zu Ihnen auf ihr Firmengelände und stellt ungefähr 30 Fragen, die sowohl organisatorischer als auch etwas technischer Natur sein können. Am Ende dieses Diagnostic wird ein Bericht verfasst und Ihnen kurze Zeit später übermittelt: er enthält eine Schätzung der Laufzeit sowie Empfehlungen zur Verbesserung der Laufzeit der Informationssicherheit.",
            },
            "service_fee": {
                "en": "The ACRC Diagnostic is available for all the companies located in Senegal and free of charge.",
                "fr": "Le Diagnostic ACRC est gratuit et possible pour toute entreprise ayant des locaux au Sénégal.",
                "de": "Der Diagnostic ist für jedes Unternehmen mit Sitz in Senegal möglich und kostenlos.",
            },
            "email_subject": {
                "en": "Request diagnostic",
                "fr": "Demander un diagnostic",
                "de": "Diagnose anfordern",
            },
            "email_body": {
                "en": "Dear ACRC Team,\n\nWe would like to request a Diagnostic ACRC from you.\n\nHere is our evaluation results identifier: {userId}\n\nHere also additional information that could be useful: \nLastname of the contact: \nFirstname of the contact: \nEmail address of the contact: \nAddress of the company for the Diagnostic (Senegal only): \nDesired language for the Diagnostic: ",
                "fr": "À l'attention de l'équipe ACRC,\n\nNous aimerions planifier un Diagnostic CASES.\n\nVoici l'identifiant lié à notre évaluation: {userId}\n\nVoici également les informations qui vous seront nécessaires: \nNom du point de contact: \nPrénom du point de contact: \nAdresse mail du point de contact: \nAdresse de l'entreprise et du Diagnostic (Senegal uniquement): \nLangue souhaitée du Diagnostic: ",
                "de": "Sehr geehrtes ACRC-Team, \n\nWir möchten ein Diagnostic ACRC mit Ihnen anfordern. \n\nHier finden Sie die ID unserer Bewertungsergebnisse: {userId} \n\nHier finden Sie auch andere nützliche Informationen: \nNachname des Kontakts: \nVorname des Kontakts: \nE-Mail-Adresse des Kontakts: \nAdresse des Unternehmens und des Ortes für den Diagnostic ACRC: (nur in Senegal): \nGewünschte Sprache für den Diagnostic ACRC:",
            },
        },
        "request_training": {
            "description": {
                "en": "Based on your score {score}, the ACRC Diagnostic is not available for your organization at this moment. We recommend you improve the information security maturity level by implementing the recommendations listed below. If you need any information security training to raise awareness in your company, do not hesitate to ",
                "fr": "Sur base de votre score de {score}, le diagnostic ACRC n'est pas disponible pour votre organisation pour le moment. Nous vous recommandons d'améliorer le niveau de maturité de la sécurité de l'information en mettant en œuvre les recommandations ci-dessous. Si vous avez besoin d'une formation à la sécurité de l'information pour sensibiliser votre entreprise, n'hésitez pas à ",
                "de": "Basierend auf Ihrem Ergebnis von {score} ist das Diagnostic ACRC derzeit für Ihr Unternehmen nicht verfügbar. Wir empfehlen Ihnen, Ihren Informationssicherheit-Reifegrad zu verbessern, indem Sie die unten aufgeführten Empfehlungen umsetzen. Wenn Sie die Informationssicherheits-Kenntnisse in Ihrem Unternehmen durch eine Schulung verbessern möchten, zögern Sie nicht ",
            },
            "let_us_know": {
                "en": "let us know.",
                "fr": "nous le faire savoir.",
                "de": "uns dies mitzuteilen.",
            },
            "email_subject": {
                "en": "Request training offer",
                "fr": "Demander une offre de formation",
                "de": "Schulungsangebot anfragen",
            },
            "email_body": {
                "en": "Dear ACRC Team, \n\nWe would like an information about security awareness training offer. \n\nHere is our evaluation results identifier: {userId} \n\nHere is also the information necessary to establish the offer: \n\nContact details: \n- Name of the contact: \n- Email address of the contact: \n\nOrganization: \n- Company Name: \n- Company address: \n- Postal code: \n- City: \n- VAT number (if applicable): \n\nTraining: \n- Number of participants*: \n- Desired language(s) for the training(s): \n- Personalized topics to discuss: \n\n* For a number of people greater than 25, the training will be done in several installments, involving a higher cost.\n",
                "fr": "À l'attention de l'équipe ACRC, \n\nNous souhaitons une offre de sensibilisation à la sécurité de l'information.\n\nVoici l'identifiant lié à notre évaluation: {userId}\n\nVoici également les informations nécessaires à l'établissement de l'offre: \n\nPoint de contact: \n- Nom du point de contact: \n- Adresse mail du point de contact: \n\nEntreprise: \n- Nom de l'entreprise: \n- Adresse de l'entreprise: \n- Adresse de l'entreprise: \n- Code postal: \n- Ville: \n- Numéro TVA (si applicable): \n\nFormations: \n- Nombre de personnes à sensibiliser*: \n- Langue(s) souhaitée(s) pour la/les formation(s): \n- Sujets personnalisés à aborder: \n\n*Pour un nombre de personnes supérieur à 25, la formation sera alors faite en plusieurs fois, impliquant un cout plus élevé.\n",
                "de": "Sehr geehrtes ACRC-Team, \n\nWir möchten ein Angebot für eine Einführung/Sensibilisierung zum Thema Informationssicherheit. \n\nHier ist die Kennung unserer Bewertung: {userId} \n\nHier finden Sie auch die Informationen, die zur Erstellung des Angebots erforderlich sind: \n\nAnlaufstelle: \n- Name der Kontaktstelle: \n- E-Mail-Adresse der Kontaktstelle: \n\nUnternehmen: \n- Name der Firma: \n- Firmenanschrift: \n- Postleitzahl: \n- Stadt: \n- Umsatzsteuer-Identifikationsnummer (falls zutreffend): \n\nAusbildung: \n- Anzahl der Teilnehmer *: \n- Gewünschte Sprache(n) für die Ausbildung(en): \n- gewünschte Themenschwerpunkte: \n\n* Wenn die Teilnehmerzahl die 25 überschreitet, wird die Schulung in mehreren Sitzungen durchgeführt, was mit höheren Kosten verbunden ist. \n",
            },
        },
        "general_feedback": {
            "button": {
                "en": "Your feedback",
                "fr": "Vos retours",
                "de": "Ihre Rückmeldung",
            },
            "title": {
                "en": "Please provide your feedback",
                "fr": "S'il vous plaît fournir vos commentaires",
                "de": "Bitte geben Sie Ihr Feedback",
            },
            "button_close": {
                "en": "Close",
                "fr": "Fermer",
                "de": "Schließen",
            },
            "button_send": {
                "en": "Send",
                "fr": "Envoyer",
                "de": "Senden",
            },
            "label": {
                "en": "Your feedback",
                "fr": "Vos retours",
                "de": "Ihre Rückmeldung",
            },
            "placeholder": {
                "en": "Please share your opinion about our tool",
                "fr": "S'il vous plaît partagez votre opinion sur notre outil",
                "de": "Bitte teilen Sie Ihre Meinung zu unserem Tool",
            },
        },
    },
    "question": {
        "continue_later": {
            "button": {
                "en": "Continue later",
                "fr": "Continuer plus tard",
                "de": "Später weitermachen",
            },
            "title": {
                "en": "Continue the evaluation later",
                "fr": "Continuer l'évaluation plus tard",
                "de": "Setzen Sie die Auswertung später fort",
            },
            "text": {
                "en": "To continue the evaluation process later you can copy the provided link, create a bookmark or use the code to resume later on the main page:",
                "fr": "Pour continuer le processus d’évaluation plus tard, vous pouvez copier le lien fourni, créer un signet ou utiliser le code pour reprendre plus tard sur la page principale:",
                "de": "Um den Evaluierungsprozess später fortzusetzen, können Sie den bereitgestellten Link kopieren und ein Lesezeichen erstellen oder verwenden Sie den Code, um später auf der Hauptseite fortzufahren:",
            },
            "button_download": {
                "en": "Download direct link",
                "fr": "Télécharger le lien direct",
                "de": "Direkten Link herunterladen",
            },
            "button_close": {
                "en": "Close",
                "fr": "Fermer",
                "de": "Schließen",
            },
        },
        "next_button": {
            "en": "Next",
            "fr": "Suite",
            "de": "Nächster",
        },
        "back_button": {
            "en": "Back",
            "fr": "Précédent",
            "de": "Bisherige",
        },
        "cancel_button": {
            "en": "Cancel",
            "fr": "Annuler",
            "de": "Stornieren",
        },
        "modify_button": {
            "en": "Modify",
            "fr": "Modifier",
            "de": "Ändern",
        },
        "description": {
            "en": "We need a little information to be able to give you useful recommendations, once the self-assessment is done.",
            "fr": "Nous avons besoin de quelques informations pour pouvoir vous faire des recommandations utiles, une fois l’auto-évaluation terminée.",
            "de": "Benötigen wir einige Informationen, um Ihnen nützliche Empfehlungen geben zu können, sobald die Selbsteinschätzung abgeschlossen ist.",
        },
        "question": {
            "en": "Question",
            "fr": "Question",
            "de": "Frage",
        },
        "title": {
            "en": "Let's start",
            "fr": "Commençons",
            "de": "Lasst uns beginnen",
        },
        "leave_survey": {
            "title": {
                "en": "Would like to leave survey?",
                "fr": "Voulez vous quitter l'enquête?",
                "de": "Möchten Sie die Umfrage verlassen?",
            },
            "yes": {
                "en": "Yes",
                "fr": "Oui",
                "de": "Ja",
            },
            "no": {
                "en": "No",
                "fr": "Non",
                "de": "Nein",
            },
        },
        "select_multi_descr": {
            "en": "Multiple answers are possible.",
            "fr": "Plusieurs réponses sont possibles.",
            "de": "ehrere Antworten sind gleichzeitig wählbar.",
        },
        "feedback_descr1": {
            "en": "This text field should not be used to answer the question.",
            "fr": "Ce champ de texte ne doit pas être utilisé pour répondre à la question.",
            "de": "Dieses Textfeld sollte nicht zur Beantwortung der Frage verwendet werden.",
        },
        "feedback_descr2": {
            "en": "Please do not provide any sensitive or confidential information refering to your identity.",
            "fr": "Veuillez ne fournir aucune donnée sensible ou confidentielle faisant référence à votre identité.",
            "de": "Bitte geben Sie keine sensiblen oder vertraulichen Datenan, die Ihre Identität veraten könnte.",
        },
    },
    "review": {
        "title": {
            "en": "Your answers review",
            "fr": "Votre aperçu des réponses",
            "de": "Ihre Antworten Vorschau",
        },
        "modify_button": {
            "en": "Modify answers",
            "fr": "Modifier les réponses",
            "de": "Ändern Sie die Antworten",
        },
        "validate_answers_button": {
            "en": "Validate answers",
            "fr": "Valider les réponses",
            "de": "Antworten validieren",
        },
    },
    "document": {
        "questions": {
            "en": "Questions",
            "fr": "Questions",
            "de": "Fragen",
        },
    },
    "form": {
        "error_messages": {
            "answer": {
                "required": {
                    "en": "You need to choose at least one answer",
                    "fr": "Vous devez choisir au moins une réponse",
                    "de": "Sie müssen mindestens eine Antwort auswählen",
                },
                "unique": {
                    "en": 'You can\'t choose multiple answers if the answer "%(value)s" is choosen',
                    "fr": 'Vous ne pouvez pas choisir plusieurs réponses si la réponse "%(value)s" est choisie',
                    "de": 'Sie können nicht mehrere Antworten auswählen, wenn die Antwort "%(value)s" ausgewählt ist',
                },
            },
        },
        "start_form": {
            "sector_question": {
                "en": "What is your sector?",
                "fr": "Quel est votre secteur?",
                "de": "Was ist Ihre Branche?",
            },
            "sector_list": {
                "BANK": {
                    "en": "Banking",
                    "fr": "Banque",
                    "de": "Banken",
                },
                "FINA": {
                    "en": "Central Bank",
                    "fr": "Banque Centrale",
                    "de": "Zentralbank",
                },
                "MIFI": {
                    "en": "Microfinance",
                    "fr": "Microfiance",
                    "de": "Mikrofinanz",
                },
                "MIAS": {
                    "en": "Micro-assurance",
                    "fr": "Microinsurance",
                    "de": "Mikroversicherung",
                },
                "MOMO": {
                    "en": "Mobile Money",
                    "fr": "Mobile Money",
                    "de": "Mobiles Geld",
                },
<<<<<<< HEAD
=======
                "BANK": {
                    "en": "Banking, insurance and real estate",
                    "fr": "Banque, assurances et immobilier",
                    "de": "Banken, Versicherungen und Immobilien",
                },
>>>>>>> 840e09c6f50082d7dbf8e700cbb56cd0d9c09331
                "SALE": {
                    "en": "Trading, sales and mass distribution",
                    "fr": "Commerce, vente et grande distribution",
                    "de": "Handel, Verkauf und Massenverteilung",
                },
                "MARK": {
                    "en": "Marketing, media and multimedia",
                    "fr": "Communication, média et multimédia",
                    "de": "Marketing, Medien und Multimedia",
                },
                "BUIL": {
                    "en": "Construction industries and civil engineering",
                    "fr": "Construction, bâtiment et travaux publics",
                    "de": "Baugewerbe und Tiefbau",
                },
                "REST": {
                    "en": "Hotel and restoration, tourism and entertainment",
                    "fr": "Hôtellerie - restauration, tourisme, loisirs et animation",
                    "de": "Hotel und Gastronomie, Tourismus und Unterhaltung",
                },
                "INDU": {
                    "en": "Industry",
                    "fr": "Industrie",
                    "de": "Industrie",
                },
                "INST": {
                    "en": "Installation and maintenance",
                    "fr": "Installation et maintenance",
                    "de": "Installation und Wartung",
                },
                "ARTI": {
                    "en": "Creation or placing of objects that are artistic and decorative",
                    "fr": "Réalisation ou placement d'objets artistiques et décoratifs",
                    "de": "Kreation oder Platzierung von künstlerischen und dekorativen Objekten",
                },
                "HEAL": {
                    "en": "Health",
                    "fr": "Santé",
                    "de": "Gesundheit",
                },
                "SERV": {
                    "en": "Home-Care Service or Community Service",
                    "fr": "Services à la personne et à la collectivité",
                    "de": "Hauspflege oder Zivildienst",
                },
                "SHOW": {
                    "en": "Shows",
                    "fr": "Spectacle",
                    "de": "Veranstaltungen",
                },
                "SUPP": {
                    "en": "Company Support",
                    "fr": "Support à l'entreprise",
                    "de": "Firmenunterstützung",
                },
                "LOGI": {
                    "en": "Transport and Logistics",
                    "fr": "Transport et logistique",
                    "de": "Transport und Logistik",
                },
                "FARM": {
                    "en": "Farming and fishing, natural spaces and green spaces, animal care",
                    "fr": "Agriculture et pêche, espaces naturels et espaces verts, soins aux animaux",
                    "de": "Landwirtschaft und Fischerei, Natur- und Grünflächen, Tierpflege",
                },
                "PUBL": {
                    "en": "Public administration",
                    "fr": "Administration publique",
                    "de": "Öffentliche Verwaltungen",
                },
                "MINE": {
                    "en": "Oil & Gas",
                    "fr": "Gaz de pétrole",
                    "de": "Ölbenzin",
                },
<<<<<<< HEAD
                "OTMI": { 
=======
                "MINE": {
>>>>>>> 840e09c6f50082d7dbf8e700cbb56cd0d9c09331
                    "en": "Other Mines",
                    "fr": "Autres mines",
                    "de": "Andere Minen",
                },
            },
            "size_question": {
                "en": "How many employees?",
                "fr": "Combien d'employés?",
                "de": "Wie viele mitarbeiter?",
            },
            "country": {
                "label": {
                    "en": "Please select your country",
                    "fr": "S'il vous plaît sélectionnez votre pays",
                    "de": "Bitte wählen Sie Ihr Land",
                },
                "required_error_message": {
                    "en": "Please select your country",
                    "fr": "S'il vous plaît sélectionnez votre pays",
                    "de": "Bitte wählen Sie Ihr Land",
                },
            },
        },
        "questions": {
            "feedback_label": {
                "en": "Your feedback",
                "fr": "Votre retour",
                "de": "Ihre Rückmeldung",
            },
            "feedback_placeholder": {
                "en": "Please let us know if anything is missing",
                "fr": "S'il vous plaît laissez-nous savoir si quelque chose est manquant",
                "de": "Bitte lassen Sie uns wissen, wenn etwas fehlt",
            },
            "custom_response": {
                "en": "Custom response",
                "fr": "Réponse personnalisée",
                "de": "Benutzerdefinierte Antwort",
            },
        },
    },
}
