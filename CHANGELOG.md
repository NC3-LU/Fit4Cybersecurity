Changelog
=========


%%version%% (unreleased)
------------------------

New
~~~
- [config] added config variable in setttings.py for wtemps. [Cédric
  Bonhomme]
- [templates] added configuration of the templates parts dir. [Cédric
  Bonhomme]
- [templates] added template part for the main logo. [Cédric Bonhomme]
- [templates] added template parts. [Cédric Bonhomme]

Changes
~~~~~~~
- [csskp core] changed admin/statistics to export/statistics in
  urlpattenrs. [Cédric Bonhomme]
- [templates] moved parts of templates. [Cédric Bonhomme]
- [config] added main_logo template path definition. [Cédric Bonhomme]
- [style] reformat files. [Cédric Bonhomme]
- [style] reformat apptags.py. [Cédric Bonhomme]
- Added custom languages in finishedSurvey. [Cédric Bonhomme]
- [documentation] Updated README file. [Cédric Bonhomme]
- [config] added countries_first to the config file. [Cédric Bonhomme]
- Added missing import for lazy_gettext and updated reporthelper.py.
  [Cédric Bonhomme]
- [configuration] updated config_dev file. [Cédric Bonhomme]
- Added a variable for the wecome message (intro text) [Cédric Bonhomme]
- [config] added csskp/static to the .gitignore file. [Cédric Bonhomme]
- [documentation] updated README. [Cédric Bonhomme]
- [config] define PROJECT_ROOT for the static files collection. [Cédric
  Bonhomme]
- [documentation] updated README. [Cédric Bonhomme]
- [documentation] Updated instructions to update the software. [Cédric
  Bonhomme]
- [documentation] Updated README. [Cédric Bonhomme]
- [config] updated settings.py. [Cédric Bonhomme]
- [models] replaced the countries with hard coded string (region: EEA,
  EU. etc.) [Cédric Bonhomme]
- Updated years of copyright in base.html. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Keep version ^1.1.1 of django-bootstrap4. [Cédric Bonhomme]
- To avoid unwanted migrations in the future, set DEFAULT_AUTO_FIELD to
  AutoField. [Cédric Bonhomme]
- Upted Django to version 3.2. [Cédric Bonhomme]
- Updated dependencies. [Cédric Bonhomme]
- [translations] generated .pot file. [Cédric Bonhomme]

Fix
~~~
- [reporthelper] use os.path.join to generate the path. [Cédric
  Bonhomme]
- [security] External links that open in a new tab or window but do not
  specify link type 'noopener' or 'noreferrer' are a potential security
  risk. [Cédric Bonhomme]
- Fix some issues with the translations: logo translations based on the
  user selection, simplify some text and updated README. [Cédric
  Bonhomme]

Other
~~~~~
- Merge branch 'fit4ilr' of github.com:CASES-LU/Fit4Cybersecurity into
  fit4ilr. [Cédric Bonhomme]
- Added reportDownload custom module. [jfrocha]
- Added the custom modules options in config file. [jfrocha]
- Removed lang references. [jfrocha]
- Added missing filter. [jfrocha]
- Merge branch 'fit4ilr' of github.com:CASES-LU/Fit4Cybersecurity into
  fit4ilr. [Cédric Bonhomme]
- Translated using Weblate (French) [Juan Rocha]

  Currently translated at 100.0% (88 of 88 strings)
- Translated using Weblate (German) [Juan Rocha]

  Currently translated at 100.0% (88 of 88 strings)
- Translate with the filter in the loop. [Cédric Bonhomme]
- Added start button when there is one unique language available.
  [jfrocha]
- Removed lang key selector. [jfrocha]
- Improved translations UI. [jfrocha]
- Merge branch 'fit4ilr' of github.com:CASES-LU/Fit4Cybersecurity into
  fit4ilr. [Cédric Bonhomme]
- Added condition when only one language is available. [jfrocha]
- Added missing gettext. [jfrocha]
- Updated translations. [jfrocha]
- Removed useless code. [Cédric Bonhomme]
- Merge branch 'fit4ilr' of github.com:CASES-LU/Fit4Cybersecurity into
  fit4ilr. [Cédric Bonhomme]
- Added custom languages in changeLang template. [jfrocha]
- Restructured code. [jfrocha]
- Added translate custom template. [Cédric Bonhomme]
- Added custom languages. [jfrocha]
- Updated gitignore and reforated with black. [Cédric Bonhomme]
- Improved get the custom configuration. [jfrocha]
- Changed location of global tool name variable. [jfrocha]
- Added missing fit4tool name tags. [jfrocha]
- Add global tag for fit4tool name. [jfrocha]
- Added missing migration. [jfrocha]
- Fixed length of country_code. [jfrocha]
- Removed last migration. [jfrocha]
- Added missing migrations by makemigration script. [jfrocha]
- Fixed the migration conflict. [Ruslan Baidan]
- Updated some question flags. [Gabriela Gheorghe]
- Added recos for questions 13 and 14. [Gabriela Gheorghe]
- Merge branch 'fit4ilr' of https://github.com/CASES-
  LU/Fit4Cybersecurity into fit4ilr. [Gabriela Gheorghe]
- Fixed the answers ids, commented out the score calculation. [Ruslan
  Baidan]
- Merge branch 'fit4ilr' of https://github.com/CASES-
  LU/Fit4Cybersecurity into fit4ilr. [Gabriela Gheorghe]
- Translated using Weblate (French) [Juan Rocha]

  Currently translated at 100.0% (18 of 18 strings)
- Translated using Weblate (German) [Juan Rocha]

  Currently translated at 100.0% (18 of 18 strings)
- Update initial_data.sql. [pundorra]

  added the questions for the survey
- Fixed conflict using their versions. [Gabriela Gheorghe]
- Conflict in readme solved. [Gabriela Gheorghe]
- Create codeql-analysis.yml. [Cedric]
- Updated Python dependencies. [Cédric Bonhomme]
- Fixed the default lang. [Ruslan Baidan]
- Changed the answers uniqueness. [Ruslan Baidan]
- Fixed the quetions translations' keys. [Ruslan Baidan]
- Reordered the migrations execution. [Ruslan Baidan]
- Added the test initial data. [Ruslan Baidan]
- Commented out the language change options. [Ruslan Baidan]
- Fit4Ilr base branch. [Ruslan Baidan]
- Removed the comment. [Ruslan Baidan]
- Implemented the functionality of free text answers. [Ruslan Baidan]
- Added the changes from the forked Fit4Privacy tool. [Ruslan Baidan]
- Updated the docker image use to the python 3.9. [Ruslan Baidan]
- Merge pull request #22 from lorisbergeron/apk-fixes. [Cedric]

  Fix missing apk issues due to python:3.8-alpine
- Fix missing apk issues due to python:3.8-alpine. [Loris Bergeron]
- Merge branch 'master' of https://github.com/CASES-
  LU/Fit4Cybersecurity. [jfrocha]
- Revert version of django-bootstrap-modal-forms to 2.1.0. [Cédric
  Bonhomme]
- Updated package.json: bootstrap and jquery. [Cédric Bonhomme]
- Added country and lang of user to the admin side. [Ruslan Baidan]
- Added the possibility to request a training. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]

  * 'master' of https://github.com/CASES-LU/CybersecurityStarterKit:
    Bumped jquery from 3.4.1 to 3.5.0.
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- Bumped jquery from 3.4.1 to 3.5.0. [Cédric Bonhomme]
- Fixed the translation, added session existance validation, updated
  authors list. [Ruslan Baidan]
- Fixed the validation of the proper user object after its modification.
  [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]

  * 'master' of https://github.com/CASES-LU/CybersecurityStarterKit:
    Updated Django and Matplotlib.
    moved definition of bootstrap4. WIP
    compile translations before launching the server
    no need to share node_modules with the host system
    createsuperuser is not idempotent: dislay a message in case of error.
    Updated README.
    Updated README.
    Updated README.
    added Docker python:3.8-alpine image. wip
- Updated Django and Matplotlib. [Cédric Bonhomme]
- Moved definition of bootstrap4. WIP. [Cédric Bonhomme]
- Compile translations before launching the server. [Cédric Bonhomme]
- No need to share node_modules with the host system. [Cédric Bonhomme]
- Createsuperuser is not idempotent: dislay a message in case of error.
  [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added Docker python:3.8-alpine image. wip. [Cédric Bonhomme]
- Added the user record lock for update when we submit question answers,
  fixed static text in the templates. [Ruslan Baidan]
- Fixed the used variable. [Ruslan Baidan]
- Changed the sort by translated text. [Ruslan Baidan]
- Added Public Sector to the organisations list and ordered them
  alphabetically. [Ruslan Baidan]
- Improved language flags (changing by svg format) [jfrocha]
- Add one step to prevent error. [jerolomb]

  prevent error during first installation
- Fixed minor issues in templates. [Cédric Bonhomme]
- Updated poetry.lock. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Reformatted with black. [Cédric Bonhomme]
- Fixed tha variable name. [Ruslan Baidan]
- Fixed the template variable. [Ruslan Baidan]
- Renamed the js folder to stats/js. [Ruslan Baidan]
- Merge pull request #14 from CASES-LU/stats. [ruslanbaidan]

  Added first files for the stats.
- Removed the print functions. [Ruslan Baidan]
- Changed the path to the stiles to use the CDN version. [Ruslan Baidan]
- Added the surveys stats. [Ruslan Baidan]
- Improved login button. [Cédric Bonhomme]
- Renamed path of the statistics page. [Cédric Bonhomme]
- Added a navbar only visible for authenticated users. [Cédric Bonhomme]
- Improved management of urls. [Cédric Bonhomme]
- Updated +LOGIN_REDIRECT_URL. [Cédric Bonhomme]
- Use the same for in order to log in the default /admin and in the new
  /admin/stats page. [Cédric Bonhomme]
- Updated login form. [Cédric Bonhomme]
- Added django-bootstrap-datepicker-plus. [Cédric Bonhomme]
- Improved login template. [Cédric Bonhomme]
- Removed useless index endpoint for stats. [Cédric Bonhomme]
- Added first files for the stats. [Cédric Bonhomme]
- Reformatted code with black. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- This is now on the wiki. [Cédric Bonhomme]
- Updated link to the source code project. [Cédric Bonhomme]
- Autodetect current version of the application. [Cédric Bonhomme]
- Updated dockerfile for poetry. [Cédric Bonhomme]
- Removed now useless files, since moved to poetry. [Cédric Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]


v1.0.1 (2020-02-14)
-------------------
- Fixed typo in CHANGELOG. [Cédric Bonhomme]
- Updated base HTML template. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Fixed issue with Django 3. Fixed security issue with Django. [Cédric
  Bonhomme]
- Merge branch 'master' into django3. [Cédric Bonhomme]
- Changed the minimum acceptable trashehold to request a diagnostic.
  [Ruslan Baidan]
- Added opining the links in new tabs. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]

  * 'master' of https://github.com/CASES-LU/CybersecurityStarterKit:
    Updated Django to handle CVE-2019-19844.
- Added Internet Explorer usage restriction on the website. [Ruslan
  Baidan]
- Merge branch 'master' into django3. [Cédric Bonhomme]
- Updated Django to handle CVE-2019-19844. [Cédric Bonhomme]
- Moved the QR code block to the text part. [Ruslan Baidan]
- Added the QR code on continue later popups during survey, review and
  results pages. [Ruslan Baidan]
- Fixed the js lib name. [Ruslan Baidan]
- Added the QR code. [Ruslan Baidan]
- Updated dependencies. [Cédric Bonhomme]
- Migration to Django 3. [Cédric Bonhomme]
- Merge pull request #11 from CASES-LU/dependabot/pip/django-2.2.8.
  [Cédric]

  Bump django from 2.2.7 to 2.2.8
- Bump django from 2.2.7 to 2.2.8. [dependabot[bot]]

  Bumps [django](https://github.com/django/django) from 2.2.7 to 2.2.8.
  - [Release notes](https://github.com/django/django/releases)
  - [Commits](https://github.com/django/django/compare/2.2.7...2.2.8)


v1.0.0 (2019-11-25)
-------------------
- Bumped version number. [Cédric Bonhomme]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Updated CHANGELOG. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Fixed the translations. [Ruslan Baidan]
- Fixed the report links. [Ruslan Baidan]
- Added general feedback forma and moved the question based feedback to
  the bottom, add tooltips for it. [Ruslan Baidan]
- Fixed the height of the feedback field. [Ruslan Baidan]
- Made the feedback filed visible by default. [Ruslan Baidan]
- Added abillity of changing language on every step, preselected
  countries in the first place. [Ruslan Baidan]
- Removed the unnecessary required filed validation translation message.
  [Ruslan Baidan]
- Removed the country blank label and set default value as "LU". [Ruslan
  Baidan]
- Added countries selection to the survey start form. [Ruslan Baidan]
- Added feedbacks displaying on the review page. [Ruslan Baidan]
- Added the translations for the feedback form. [Ruslan Baidan]
- Renamed the preview action to review, added the questions feedback
  functionality, improved the admin UI. [Ruslan Baidan]
- Refactored the survey process to allow user go back and change
  answers, added a preview page. [Ruslan Baidan]
- Moved the robots.txt to the static folder. [Ruslan Baidan]
- Added robots.txt. [Ruslan Baidan]
- Added the progress bar the questions progress page. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Updated translations in po files. [Cédric Bonhomme]
- Fixed some translations. [Cédric Bonhomme]


v0.0.2 (2019-11-13)
-------------------
- Added the UI to prevent the unexpected answers selection. [Ruslan
  Baidan]
- Added redirection to finish survey page when user completed survey.
  [Ruslan Baidan]
- Styles fixes for results page, report logo now depends on selected
  language, improved the report file name. [Ruslan Baidan]
- Updated the user restore session links. [Ruslan Baidan]
- Added hashing the user id securelly send it via email. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Added multilang templates. [Fabien Mathey]
- Fixed the surver resume issue, when we could inject braking string.
  [Ruslan Baidan]
- Updated the translations for results chart. [Ruslan Baidan]
- Changed the charts to show in percentage per section, removed max
  sections figure. [Ruslan Baidan]
- Grouped displaying of the recommendations by category on results and
  report page. [Ruslan Baidan]
- Replaced the sectors with the new ones, changed users' creation only
  after submitting the start question, fixed migrations. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- User score must be at least min_acceptable_score. [Cédric Bonhomme]
- Moved some important variables in congig_dev.py. [Cédric Bonhomme]
- Fixed the users answers selection in the report. [Ruslan Baidan]
- Fixed the translation. [Ruslan Baidan]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Completed translations. [Cédric Bonhomme]
- Removed ueless variable. [Cédric Bonhomme]
- Completed translations. [Cédric Bonhomme]
- Typos and translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Updated headers and rel link for apple-touch-icon. [Cédric Bonhomme]
- Set version to 0.0.0 when file is not found. [Cédric Bonhomme]
- Uses BASE_DIR to find the VERSION.json file. [Cédric Bonhomme]
- Fixed the email sending and translations for the parts. [Ruslan
  Baidan]
- Fix. [Cédric Bonhomme]
- Added a context processor in order to make the app version available
  to every template. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- User score must be at least min_acceptable_score. [Cédric Bonhomme]
- Added a temporary solution of the mail sending in case if the score is
  lover then 80 points. [Ruslan Baidan]
- Fixed the worng model key. [Ruslan Baidan]
- Removed the prints. [Ruslan Baidan]
- Added missed translations logic to the report. [Ruslan Baidan]
- Added optional usage of apache on docker and removed reversing of the
  categories of chart. [Ruslan Baidan]
- Temporary fix. [Cédric Bonhomme]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Updated README (deployment instructions). [Cédric Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Add the possibility to custom BOOTSTRAP4 configuration variable via
  the config module. [Cédric Bonhomme]
- Fixed favicon link. [Ruslan Baidan]
- Adde the prompt popup to prevet immidiate redirection to the home
  page, added button disabling when questions are not chosen. [Ruslan
  Baidan]
- Updated template.docx. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Changed the report to make the whole line bold when answer is
  selected. [Fabien Mathey]


v0.0.1 (2019-10-22)
-------------------

Changes
~~~~~~~
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]
- [tranlsation] minor fixes for French translations. [Cédric Bonhomme]

Other
~~~~~
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- German result text done. [Fabien Mathey]
- Corrected Typo. [Fabien Mathey]
- Added german recs text. [Fabien Mathey]
- Added CHANGELOG. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- Added german intro. [Fabien Mathey]
- Updated english intro. [Fabien Mathey]
- Commented STATIC_ROOT in settings.py. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- Translation done english description. [Fabien Mathey]
- Corrected spelling. [Fabien Mathey]
- Corrected french version. [Fabien Mathey]
- Translated german description. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Translations in German verified - SQL file. [Fabien Mathey]
- Copy static files required by Django Admin. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Merge branch 'master' of https://github.com/CASES-
  LU/CybersecurityStarterKit. [Ruslan Baidan]
- Reduced the logo size. [Ruslan Baidan]
- Finished english revision of SQL file. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Replace the apache usage instead of python server for docker env.
  [Ruslan Baidan]
- Improved footer. [Cédric Bonhomme]
- Improved footer. [Cédric Bonhomme]
- Improved footer. [Cédric Bonhomme]
- Hide logo on sceens smaller than md. [Cédric Bonhomme]
- Improved layout of the logo. [Cédric Bonhomme]
- Removed useless import. [Cédric Bonhomme]
- Updated README> [Cédric Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Added example dev conf file. [Cédric Bonhomme]
- Fixed tabulation. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/Fit4Cybersecurity.
  [Cédric Bonhomme]
- Updated ALLOWED_HOSTS. [Cédric Bonhomme]
- Continued english translations. [Fabien Mathey]
- Continued translations. [Fabien Mathey]
- Translations EN and DE revised for Questions and answers. [Fabien
  Mathey]
- Improved ToS. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Now using pipenv instead of using pip. [Cédric Bonhomme]
- Removed extrat spaces. [Cédric Bonhomme]
- Added COPYING file. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Fixed the form elements displaying after the validation. [Ruslan
  Baidan]
- Improved footer. [Cédric Bonhomme]
- Fixed fr translation. [Cédric Bonhomme]
- Added custom spacers. [Cédric Bonhomme]
- Removed the bright blue blackground. [Cédric Bonhomme]
- Take benefit of Django template inheritance. [Cédric Bonhomme]
- Fixed the buttons styles. [Ruslan Baidan]
- Corrected translations. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Fixed an error in the template and added a terms page with a link in
  the footer. [Cédric Bonhomme]
- More translations fixes. [Cédric Bonhomme]
- More translations fixes. [Cédric Bonhomme]
- Updated french translations. [Cédric Bonhomme]
- Completed some translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Fix wrong french translations in the index template. [Cédric Bonhomme]
- Fix wrong french translations. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Cédric Bonhomme]
- Added SVG files of Logos and some translations are corrected. [Fabien
  Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Updated some english and german translations. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Cédric Bonhomme]
- Replaced french word 'Prochain' by 'Suite'. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Cédric Bonhomme]
- Not raising here. [Cédric Bonhomme]
- Replaced Logos with translated ones. [Fabien Mathey]
- Merged. [Fabien Mathey]
- Added english translations for those parts. [Ruslan Baidan]
- Added comments + handle the exception returnd by generate_chart_png.
  [Cédric Bonhomme]
- Handles error when matplotlib is not able to write in the folder
  dedicated to the user's pictures. [Cédric Bonhomme]
- Fixed bad merge. [Cédric Bonhomme]
- Some small corrections. [Fabien Mathey]
- Merged the docker fix. [Fabien Mathey]
- Finished the translations of recommendations and added the choosen
  lang for getting the list. [Ruslan Baidan]
- Merge branch 'scoredev' of https://github.com/CASES-
  LU/CybersecurityStarterKit into scoredev. [Ruslan Baidan]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Checks if the psql command is already available. [Cédric Bonhomme]
- Removed temporary files. [Ruslan Baidan]
- Fixed the whole docker stuff. [Fabien Mathey]
- Added missing postgressql client packages and forced the python3
  usage. [Fabien Mathey]
- Added new content and value. [Fabien Mathey]
- Finished french text for the report. [Fabien Mathey]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Fabien Mathey]
- Added wait for postgres container start script. [Ruslan Baidan]
- Merge branch 'scoredev' of https://github.com/CASES-
  LU/CybersecurityStarterKit into scoredev. [Ruslan Baidan]

  # Conflicts:
  #	.gitignore
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Moved useful resources in a dedicated file. [Cédric Bonhomme]
- Updated .gitingore. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Changed the form field type to radiogroup for single question types.
  [Ruslan Baidan]
- Recommendations combined and document corrected. [Fabien Mathey]
- Finished the initial data migration script. [Ruslan Baidan]
- Fixed the migration script. [Ruslan Baidan]
- Merge branches 'scoredev' and 'scoredev' of https://github.com/CASES-
  LU/CybersecurityStarterKit into scoredev. [Ruslan Baidan]

  # Conflicts:
  #	package.json
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Removed a useless library fron package.json. [Cédric Bonhomme]
- Ignore sqlite dabase. [Cédric Bonhomme]
- Removed npm and fixed the migration. [Ruslan Baidan]
- Added the initial data migration script. [Ruslan Baidan]
- Cleaned up the package.json and added .lock to the repo. [Ruslan
  Baidan]
- Removed Sqllite db. [Ruslan Baidan]
- Replaced external static with cdn links. [Ruslan Baidan]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Make document nicer. [Fabien Mathey]
- Added better template and recommendations to report. [Fabien Mathey]
- Deleted file. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Changed directory where npm writes JS dependencies wit the option
  --prefix. [Cédric Bonhomme]
- Merge branch 'scoredev' of https://github.com/CASES-
  LU/CybersecurityStarterKit into scoredev. [Ruslan Baidan]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Using psycopg2-binary. [Cédric Bonhomme]
- Restructurd the app. [Ruslan Baidan]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Dockerized the app. [Ruslan Baidan]
- Fixed error in package.json. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Little 'cosmethic' change. [Cédric Bonhomme]
- Updatd French translations. [Cédric Bonhomme]
- Updated translations for the logo. [Cédric Bonhomme]
- Added logo to translates. [Cédric Bonhomme]
- Initialization of translations with i18n. [Cédric Bonhomme]
- Handle some exceptions when a translation is not done yet or a
  template is not present. [Cédric Bonhomme]
- Oops. [Cédric Bonhomme]
- Added missing subcommand. [Cédric Bonhomme]
- Fix links. [Cédric Bonhomme]
- Updated README mainly because we now need to locally install
  JavaScript dependencies with npm. [Cédric Bonhomme]
- Make JavaScript and CSS dependencies local. [Cédric Bonhomme]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Translated the start survey form. [Ruslan Baidan]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Cédric Bonhomme]
- Fixed the popups massages and styles, added the proper forms
  validation and translated messages, left a single document for
  generation. [Ruslan Baidan]
- Fixed merged. [Cédric Bonhomme]
- Added the generated chart image to the report. [Ruslan Baidan]
- Moved the matplotlib png generation to the report helper, some code
  fixes. [Ruslan Baidan]
- Merge branch 'scoredev' of github.com:CASES-LU/CybersecurityStarterKit
  into scoredev. [Fabien Mathey]
- Merge remote-tracking branch 'origin/master' into scoredev. [Ruslan
  Baidan]

  # Conflicts:
  #	csskp/survey/viewLogic.py
- Removed docx-mailmerge dependency. [Ruslan Baidan]
- Added chart.js radar stuff. [Fabien Mathey]
- Added sections name list to result calculation. [Fabien Mathey]
- Fixed an error during the last merge. [Cédric Bonhomme]
- Fixed conflict. [Cédric Bonhomme]
- Fixed path for the templates of reports. [Cédric Bonhomme]
- Using container instead of container-fluid. [Cédric Bonhomme]
- Restored database. [Fabien Mathey]
- Merge updated. [Fabien Mathey]
- Merged master branch into this one and resolved some issues. [Ruslan
  Baidan]
- Added the Radar chart util and test data to generate the chart.
  [Ruslan Baidan]
- Removed pylab requirements. [Cédric Bonhomme]
- Added pylab requirements. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Cédric Bonhomme]
- Removed the extra static folder. [Ruslan Baidan]
- Added baseic Matplotlib example. [Cédric Bonhomme]
- Removed extra import sections. [Ruslan Baidan]
- Pushed the renamed template. [Ruslan Baidan]
- Added the warning messages in case we don't find a key to resume,
  simplified URLs and removed id param from /question url, fixed the
  issue with navigation back during survey. [Ruslan Baidan]
- Finished theory on document creation - now testing. [Fabien Mathey]
- Added some lines to the report generation. [Fabien Mathey]
- Score stuff advanced. [Fabien Mathey]
- Score devs started to evaluate responses. [Fabien Mathey]
- Some more css adaptations and some translations corrections. [Fabien
  Mathey]
- Made the initial screen more beautiful - a long way to go! [Fabien
  Mathey]
- Added UI translations and some beauty stuff. [Fabien Mathey]
- Added some beautifying css stuff. [Fabien Mathey]
- Added files and updated sources. [Fabien Mathey]
- Table insertion now works - image still not really. [Fabien Mathey]
- Updated readme with some links for document docx generation. [Fabien
  Mathey]
- Report generation working now by pressing button. [Fabien Mathey]
- Document generation works now. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Removed the renamed files. [Ruslan Baidan]
- Added the popup box to resume the survey process. [Ruslan Baidan]
- Recommendations getting logic now working - need to make templates
  now. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Fixed the redirection to the user's current evaluation progress.
  [Ruslan Baidan]
- Added the modal form with possibility to continue later, added process
  of the continue later request. [Ruslan Baidan]
- Removed un used declation. [Fabien Mathey]
- Shit works now: translation, forms and savings of questions. [Fabien
  Mathey]
- Forms are invalid when submitted. [Fabien Mathey]
- Merge branch 'master' of github.com:CASES-LU/CybersecurityStarterKit.
  [Fabien Mathey]
- Added pipfile and the bootstrap4 configuration. [Ruslan Baidan]
- Added good stuff and killed the whole database migration - not quite
  working yet. [Fabien Mathey]
- Fixed multi lingual stuff. [Fabien Mathey]
- JUST A BACKUP - FUNCT. NOT TESTED - converted the whole thing to allow
  multi lingual stuff. [Fabien Mathey]
- Fixed the save everys answer n times by correcting the loop. [Fabien
  Mathey]
- Removed some spaces. [Fabien Mathey]
- Saving the question the user is at and set the state when the
  questions are all done. [Fabien Mathey]
- Saving the initial question now works. [Fabien Mathey]
- Added answers fields for the initial questions in user model. [Fabien
  Mathey]
- Fixed the displaying in the admin panel. [Fabien Mathey]
- Fixed the save the answers to the questions in the - not the firest
  one yet. [Fabien Mathey]
- Added save function for answers - missing still initial question save.
  [Fabien Mathey]
- Updated how the questions are loaded and used. [Fabien Mathey]
- Added some descriptive comments. [Fabien Mathey]
- Inserted question type, and ordering indexes for question and answer.
  [Fabien Mathey]
- Added how to use and test the python implementation to the README.
  [Fabien Mathey]
- Give question type and index to questions and answers. [Fabien Mathey]
- Added admin panel and getting questions from DB now. [Fabien Mathey]
- Changed the logic to new file (outside of view) [Fabien Mathey]
- Changed comment to make more sense. [Fabien Mathey]
- Added some logic to start the survey and go to first quesiton. [Fabien
  Mathey]
- Removed the pass from the def. [Fabien Mathey]
- Added the current question field. [Fabien Mathey]
- Added models and url paths. [Fabien Mathey]
- Added python version. [Fabien Mathey]
- Initial zend framework skeleton application creation. [Fabien Mathey]
- Installation documentation continued with the initial setup. [Fabien
  Mathey]
- Added composer to the apt get list. [Fabien Mathey]
- CHange Config to prepare for ZEND. [Fabien Mathey]
- Initial readme. [Fabien Mathey]
- Initial commit. [Fabien Mathey]


