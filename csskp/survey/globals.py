
SECTOR_CHOICES = [
    ("gov","Government"),
    ("adm","Public Administrations"),
    ("fin","Sinancial Sector"),
    ("it", "Information Technology (IT)"),
]

COUNTRIES = [
    ("LU","Luxembourg"),
    ("DE","Deutschland"),
    ("BE","Belgique"),
    ("FR","France"),
]

SERVICE_TARGETS = [
    ("SME", "Small to Medium Size Entreprises"),
    ("BC", "Big Company"),
    ("MN", "Multinationals Coorporations"),
    ("IND", "Independent"),
    ("PRI", "Private Person"),
]

COMPANY_SIZE = [
    ("a","1-5"),
    ("b","6-10"),
    ("c","10-20"),
    ("d","20-50"),
    ("e","50-100"),
    ("f","100-200"),
    ("g","200-500"),
    ("h","500-1000"),
    ("i","1000-5000"),
    ("j","5000+"),
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
    ("Q"," Question"),
    ("A", "Answer"),
    ("R", "Recommendation"),
    ("S", "Question Section"),
    ("C", "Company Service Category"),
]

TRANSLATION_UI = {
    'report': {
        'download': {
            'en':"Download",
            'fr':"Téléchargement",
            'de':"Herunterladen",
        },
        'report': {
            'en':"Summary",
            'fr':"Résumé",
            'de':"Zusammenfassung",
        },
        'description': {
            'en':"This is the list of recommendations to improve the information security maturity in your company, provided that your answers did correctly reflect the state in your company. Also keep in mind that it is a self-assessment and only scratches the surface of the information security maturity level and thus, we are not liable for the results of this survey.",
            'fr':"Voici la liste des recommandations visant à améliorer la maturité de la sécurité de l'information dans votre entreprise, à condition que vos réponses reflètent correctement l'état de votre entreprise. N'oubliez pas non plus qu'il s'agit d'une auto-évaluation et qu'elle ne fait qu'effleurer le niveau de maturité de la sécurité de l'information. Par conséquent, nous ne sommes pas responsables des résultats de cette enquête.",
            'de':"Dies ist die Liste der Empfehlungen zur Verbesserung der Informationssicherheitsreife in Ihrem Unternehmen, sofern Ihre Antworten den Status in Ihrem Unternehmen korrekt widerspiegeln. Denken Sie auch daran, dass es sich um eine Selbsteinschätzung handelt, die nur die Oberfläche des Reifegrads der Informationssicherheit abbilden kann, und wir daher nicht für die Ergebnisse dieser Umfrage haften.",
        },
        'title': {
            'en':"final summary",
            'fr':"résumé final",
            'de':"Zusammenfassung",
        },
    },
    'question':{
        'continuelater': {
            'en':"continue later",
            'fr':"continuer plus tard",
            'de':"später weitermachen",
        },
        'descripition': {
            'en':"Before we start, we need a little information to be able to give you useful recommendations, once the self-assessment is done.",
            'fr':"Avant de commencer, nous avons besoin de quelques informations pour pouvoir vous faire des recommandations utiles, une fois l’auto-évaluation terminée.",
            'de':"Bevor wir beginnen, benötigen wir einige Informationen, um Ihnen nützliche Empfehlungen geben zu können, sobald die Selbsteinschätzung abgeschlossen ist.",
        },
        'question': {
            'en':"Question",
            'fr':"Question",
            'de':"Frage",
        },
        'title': {
            'en':"Let's start",
            'fr':"Commençons",
            'de':"Lasst uns beginnen",
        },
    }
}