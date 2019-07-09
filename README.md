# CybersecurityStarterKit
New PHP implementation with many more features and simplified questions compared to the Startup security kit

#### Installing LAMP and Zend 3:

```bash
apt install apache2 mysql-server php7.2 libapache2-mod-php7.2 php-mysql composer
``` 

Then adapt the configuration `/etc/apache2/apache2.conf` and change in the `<directory /var/www>` tag `AllowOverride` to

```apache
AllowOverride FileInfo
```

Alternatively, you can do that in the apache webside config as we need to allow for .htaccess files to be active.

