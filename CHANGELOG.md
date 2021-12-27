Changelog
=========


%%version%% (unreleased)
------------------------

New
~~~
- [templates] added new maintenance task in admin panel. [Cédric
  Bonhomme]
- [templates] added new maintenance task in admin panel. [Cédric
  Bonhomme]
- [admin] it is now possible to export the survey via HTTP request.
  [Cédric Bonhomme]
- [commands] Added basic command to export a survey. Generates a file
  compatible with the import_questions command. [Cédric Bonhomme]
- [vm] added new packer configuration. [Cédric Bonhomme]
- [logo] Added fit4operatorsurvey logo. [jfrocha]
- [filter] added new filter to find elem in list of tuples. [Cédric
  Bonhomme]
- [core] added new get_obj_attr filter. [Cédric Bonhomme]
- [API] added new API endpoint in order to manage translations. [Cédric
  Bonhomme]
- [translations] added page to list the remaining strings to translalte.
  [Cédric Bonhomme]
- [translations] added page to manage the translations. [Cédric
  Bonhomme]
- [data] added JSON file for survey4operators. [Cédric Bonhomme]
- [core] added new translate_db Django filter. [Cédric Bonhomme]
- [core] added Django command to import translations. [Cédric Bonhomme]
- [email] added email templates and modal to enter the email address.
  [Cédric Bonhomme]
- [utils] added a function to send report per emails. [Cédric Bonhomme]
- [report] added PDF report generation. [Cédric Bonhomme]
- [config] added config variable in setttings.py for wtemps. [Cédric
  Bonhomme]
- [templates] added configuration of the templates parts dir. [Cédric
  Bonhomme]
- [templates] added template part for the main logo. [Cédric Bonhomme]
- [templates] added template parts. [Cédric Bonhomme]

Changes
~~~~~~~
- [dependencies] Updated fork-awesome. [Cédric Bonhomme]
- [style] Reformat with black. [Cédric Bonhomme]
- [dependencies] Updated Numpy. [Cédric Bonhomme]
- [style] format code with black. [Cédric Bonhomme]
- [templates] added survey result column in the admin page. [Cédric
  Bonhomme]
- [core] calculateResult is not using the lang parameter. [Cédric
  Bonhomme]
- [admin] improved management of commands executed in a subprocess.
  [Cédric Bonhomme]
- [templates] improved customization in the Django admin area. [Cédric
  Bonhomme]
- [style] format code with black. [Cédric Bonhomme]
- [templates] removed useless messages section in the admin template.
  [Cédric Bonhomme]
- [style] format code with black. [Cédric Bonhomme]
- [templates] added option to generate mo files from the admin page.
  [Cédric Bonhomme]
- [templates] updated default index Django admin template in order to
  add links to different admin tools. [Cédric Bonhomme]
- [stats] Updated and fixed an issue with django-bootstrap-datepicker-
  plus. [Cédric Bonhomme]
- [style] format code with black. [Cédric Bonhomme]
- [stats] continue on questions with 0 points. [Cédric Bonhomme]
- [commands] added the possibility to export objects with database ids.
  [Cédric Bonhomme]
- [core] django.views.i18n.set_language() no longer set the user
  language in request.session (key
  django.utils.translation.LANGUAGE_SESSION_KEY was deprecated, now it
  has been removed). [Cédric Bonhomme]
- [core] updated dependencies. [Cédric Bonhomme]
- [matplotlib] When using Matplotlib in a web server with Apache it is
  strongly recommended to not use pyplot (pyplot maintains references to
  the opened figures). [Cédric Bonhomme]
- [commands] Simplified import_questions command. [Cédric Bonhomme]
- [translations] updated some french translations. [Cédric Bonhomme]
- [style] reformated with black. [Cédric Bonhomme]
- [mypy] mypy.ini is now useless. [Cédric Bonhomme]
- [utils] added function to check if possible to redirect. [Cédric
  Bonhomme]
- [logging] fixed logging mechanism. [Cédric Bonhomme]
- [dependencies] updated typing-extensions. [Cédric Bonhomme]
- [dependencies] prevent the installation of 3.0.6 yanked release of
  django-bootstrap-datepicker-plus https://github.com/python-
  poetry/poetry/issues/2453. [Cédric Bonhomme]

  (cherry picked from commit cc0c93beb5506e884cf846a00b27883566667e45)
- [security] URL redirection based on unvalidated user input may cause
  redirection to malicious web sites. [Cédric Bonhomme]

  (cherry picked from commit e485c18762f290cf511b356b9f36fa58e19bd631)
- [security] interpret target as a CSS selector not as HTML. [Cédric
  Bonhomme]

  (cherry picked from commit 65c7258d9b00abcc6eb602f77957373b07fd2af1)
- [report] improved the generation of the chart for the report. [Cédric
  Bonhomme]
- [dependencies] bumped dependencies for better compatibility with
  Python 3.10.0. [Cédric Bonhomme]
- [report] the email address of the recipient is now sent in the body of
  the request with CSRF token. [Cédric Bonhomme]
- [vm] clean the directoy after VN generation. [Cédric Bonhomme]
- [vm] computed installer checksums. [Cédric Bonhomme]
- [vm] get the hostname of the VM for the list of allowed hosts. [Cédric
  Bonhomme]
- [vm] added systemd service in postinstall.sh. [Cédric Bonhomme]
- [vm] fixed an issue with second provisionner. [Cédric Bonhomme]
- [vm] updated install script with database creation. [Cédric Bonhomme]
- [packer] added post-processors for the checksums. [Cédric Bonhomme]
- [logo] Changed type of logo fit4operator. [jfrocha]
- [dependencies] Bumped version of numpy. [Cédric Bonhomme]
- Moved mypy in tool.poetry.dependencies. [Cédric Bonhomme]
- [models] example on how to make class objects JSON serializable (with
  a right mixin). [Cédric Bonhomme]
- [documentation] Updated doc related to certbot. [Cédric Bonhomme]
- [documentation] Typo. [Cédric Bonhomme]
- [documentation] Typo. [Cédric Bonhomme]
- [documentation] Imporved documentation in the README. [Cédric
  Bonhomme]
- [report] Improved context. [jfrocha]
- [importer] reformat. [Cédric Bonhomme]
- [importer] count the number of imported objects. [Cédric Bonhomme]
- [API] updated endpoint of the Translation API and added OpenAPI
  Schema. [Cédric Bonhomme]
- [documentation] Updated readme with information on the configuration
  file. [Cédric Bonhomme]
- Updated with changes from branch fitcyber4africa. [Cédric Bonhomme]
- Custom admin template for translations. [Cédric Bonhomme]
- [translations] updated translation mechanism. The table Translation
  now contains only translations and classes directly related to the
  main business objects are using a 'label' property for the default
  language. [Cédric Bonhomme]
- [notifications] make the sending of the emails async. [Cédric
  Bonhomme]
- [typy] enriched typing information. [Cédric Bonhomme]
- Export of translations. [Cédric Bonhomme]
- [core] Moved deprecated SQL dump in data/fit4ilr. [Cédric Bonhomme]
- [documentation] Updated README. [Cédric Bonhomme]
- [commands] Added a command to import data in the database. wip.
  [Cédric Bonhomme]
- [utils] updated email sending, new configuration for the SMTP server
  are now required. [Cédric Bonhomme]
- [lib] send PDF report as an attachment to the email. [Cédric Bonhomme]
- [utils] Added function to send emails. [Cédric Bonhomme]
- [report] decode the base64 string. [Cédric Bonhomme]
- [template] added form-control CSS class to date picker. [Cédric
  Bonhomme]
- [template] removed logo from stats export page. [Cédric Bonhomme]
- [template] copyright are for humans and establishes how far back the
  claim is made for a version. [Cédric Bonhomme]
- [config] Check if conf variables are defined when importing in
  settings.py. [Cédric Bonhomme]
- Added missing translation. [Cédric Bonhomme]
- [ci] exit with error code when flake8 checks failed. [Cédric Bonhomme]
- [ci] Added Python 3.10.0 to matrix:python-version. [Cédric Bonhomme]
- [core] Removed now useless/dead code. [Cédric Bonhomme]
- [templatetags] add ifinlist filter. [Cédric Bonhomme]
- [report] Moved the definition of the filter format_datetime. [Cédric
  Bonhomme]
- [report] Tell Django to render the Web link in the variable. [Cédric
  Bonhomme]
- [report] HTML report is now generate with Django own engine. [Cédric
  Bonhomme]
- [report] insert survey questions in the report (separate data and HTML
  format) [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Minimal_acceptable_score must be present in config.py. Updated some
  translations. [Cédric Bonhomme]
- [style] reformat with black. [Cédric Bonhomme]
- [report] test templute include for footer. [Cédric Bonhomme]
- Logo are now local. [Cédric Bonhomme]
- [report] tested inclusion of the generated chart and the list of
  recommendations. [Cédric Bonhomme]
- [report] testing internationalization in the Jinja template. [Cédric
  Bonhomme]
- [report] testing custom Jinja global variables for the report
  generation. [Cédric Bonhomme]
- [report] testing custom Jinja filters for the report generation.
  [Cédric Bonhomme]
- Restore check of the language translation key. [Cédric Bonhomme]
- Django compatibility with Python 3.10. [Cédric Bonhomme]
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
- [report] in generate_chart_png, ensures that x and y have same first
  dimension. Log the eventual error. Removed useless lang parameter in
  genera_chart_png. [Cédric Bonhomme]
- [packer] fixed path to the git4cybersecurity related data. [Cédric
  Bonhomme]
- [config] fixed a typo in the default config file in INSTALL.sh.
  [Cédric Bonhomme]
- [templates] Fixed type in admin/views.py and removed useless stuff in
  templates. [Cédric Bonhomme]
- [typing] exec_cmd_no_wait type is None and not NoReturn. [Cédric
  Bonhomme]
- [commands] added missing maxPoints of the question. [Cédric Bonhomme]

  (cherry picked from commit 7df38d5bdcf51265fdc1eedefacab3dd48715892)
- [templates] CSS for the PDF generation was not found when used with
  mod_wsgi. [Cédric Bonhomme]
- [lint] fixed flake8 error. [Cédric Bonhomme]
- Error: "Sequence[str]" has no attribute "append" [Cédric Bonhomme]
- [email] fixed error in email templates and added an option to
  deactivate the sending of report via email. [Cédric Bonhomme]
- [emails] fix wrong import. [Cédric Bonhomme]
- Fixed some mypy warnings. removed useless code and fixed chart's
  legend. [Cédric Bonhomme]
- [style] fixed a flake warning. [Cédric Bonhomme]
- [templates] fixed nav-bar menu in the export stats page. [Cédric
  Bonhomme]
- [template] fixed nav-bar dropdown menu. [Cédric Bonhomme]
- [core] Fixed some routing issues. [Cédric Bonhomme]
- [flake8] 'django.utils.translation.gettext as _' imported but unused.
  [Cédric Bonhomme]
- [config] added the missing change for the templates_parts_dir. [Cédric
  Bonhomme]
- [templates] fixed a routing issue in csskp/urls.py and improved
  templates parts. [Cédric Bonhomme]
- [type] fixed some types definitions. [Cédric Bonhomme]
- Fixed mypy issue. Rename config_prod.py to config.py on your local
  instance. [Cédric Bonhomme]
- [reporthelper] use os.path.join to generate the path. [Cédric
  Bonhomme]
- [security] External links that open in a new tab or window but do not
  specify link type 'noopener' or 'noreferrer' are a potential security
  risk. [Cédric Bonhomme]
- Fix some issues with the translations: logo translations based on the
  user selection, simplify some text and updated README. [Cédric
  Bonhomme]


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


