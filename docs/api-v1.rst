API v1
======

The API version 1 uses the OpenAPI Specification for its documentation.


.. literalinclude:: static/openapi-schema.yml
   :language: yaml
   :linenos:
   :caption: OpenAPI Schema



Updating the OpenAPI Schema
===========================

If you have updated the API, you can generate a new OpenAPI Schema:

```bash
$ python manage.py generateschema --file docs/static/openapi-schema.yml
```
