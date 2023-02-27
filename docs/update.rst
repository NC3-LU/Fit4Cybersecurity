Upgrading the application
=========================

.. code-block:: bash

    $ cd Fit4Cybersecurity/
    $ git pull origin master --tags
    $ npm ci
    $ poetry install --no-dev
    $ poetry run python manage.py collectstatic
    $ poetry run python manage.py migrate
    $ poetry run python manage.py compilemessages


Updating the translations
=========================

If you want to update the translations (in the case **you have locally**
changed the source code), you must first run:

.. code-block:: bash

    $ python manage.py makemessages -a --keep-pot -e html,txt,py,json


Then you can use a tool like
[poedit](https://poedit.net) to translate the strings and you can compile with
the previously mentioned command.

If you want to re-generate the .pot template file:

.. code-block:: bash

    $ python manage.py makemessages -a --keep-pot
