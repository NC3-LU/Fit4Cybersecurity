# CybersecurityStarterKit
New PHP implementation with many more features and simplified questions compared to the Startup security kit

## Python/Django Installation

Just install `Python 3` (incl. `python-lxml`) and `Django 2.2`,

Then clone this repository and install all the packages in the Pipfile. 

#### Running the test server

For the next step, if you want to test the project and your modification, use the terminal and go into the folder `csskp`. And then simply run the test server:

```bash
python3 manage.py runserver
```

#### updated the models?
If you made any changes to the database structure (models) then you need to do the following:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```


#### Sources
[1] https://pbpython.com/python-word-template.html
[2] https://stackoverflow.com/questions/19400089/downloadable-docx-file-in-django
[3] https://stackoverflow.com/questions/54260657/python-script-insert-image-using-mailmerge-into-docx-file
[4] https://pypi.org/project/docx-mailmerge/
[5] https://python-docx.readthedocs.io/en/latest/



## PHP version install - not maintained at the moment

#### Installing LAMP and Zend 3 from scratch:

```bash
apt install apache2 mysql-server php7.2 libapache2-mod-php7.2 php-mysql composer zendframework zend-framework zend-framework-bin
``` 

Then adapt the configuration `/etc/apache2/apache2.conf` and change in the `<directory /var/www>` tag `AllowOverride` to

```apache
AllowOverride FileInfo
```

Alternatively, you can do that in the apache webside config as we need to allow for .htaccess files to be active.

#### Apache 2 config

Be careful to configure the apache system in a way that it knows that the accessible portion is in the `public` folder.

#### Initial Zend installation:

* Do you want a minimal install (no optional packages)? Y/n **n**
* Would you like to install the developer toolbar? y/N **y**
* Would you like to install caching support? y/N **y**
* Would you like to install database support (installs zend-db)? y/N **y**
* Would you like to install forms support? y/N **n**
* Would you like to install JSON de/serialization support? y/N **y**
* Would you like to install logging support? y/N **y**
* Would you like to install MVC-based console support? (We recommend migrating to zf-console, symfony/console, or Aura.CLI) y/N **n**
* Would you like to install i18n support? y/N **y**
* Would you like to install the official MVC plugins, including PRG support, identity, and flash messages? y/N **y**
* Would you like to use the PSR-7 middleware dispatcher? y/N **n**
* Would you like to install sessions support? y/N **y**
* Would you like to install MVC testing support? y/N **y**
* Would you like to install the zend-di integration for zend-servicemanager? y/N **n**

```bash
Please select which config file you wish to inject 'ZendDeveloperTools' into:
  [0] Do not inject
  [1] config/modules.config.php
  [2] config/development.config.php.dist
  Make your selection (default is 0): 2
```

The rest will be simply added to the `modules.config.php`
