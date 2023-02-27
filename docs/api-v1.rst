API v1
======

The API version 1 uses the OpenAPI Specification for its documentation.
You can directly interect with the API documentation:

- OpenAPI schema: http://127.0.0.1:8000/survey/api/v1/schema/
- Swagger UI: http://127.0.0.1:8000/survey/api/v1/swagger-ui/
- Redoc: http://127.0.0.1:8000/survey/api/v1/redoc/


.. literalinclude:: static/openapi-schema.yml
   :language: yaml
   :linenos:
   :caption: OpenAPI Schema


Updating the OpenAPI Schema
===========================

If you have updated the API, you can generate a new OpenAPI Schema:

.. code-block:: bash

    $ python manage.py spectacular --format openapi --file docs/static/openapi-schema.yml

This file is included in the documentation of Fit4Cybersecurity.
