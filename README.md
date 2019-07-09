# CybersecurityStarterKit
New PHP implementation with many more features and simplified questions compared to the Startup security kit

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
