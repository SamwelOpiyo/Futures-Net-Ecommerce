Creating a Product
==================

Using Swagger API Docs
----------------------

Click on API to Extend it.

* When creating any request, remember to always set version to v1.

Create Product Category
^^^^^^^^^^^^^^^^^^^^^^^

Extend POST - /api/{version}/product-categories/

Click Try it out.

Fill in version to v1.

Input the following json data.

::

    {
        "category_name": "Fashion"
    }
then click on execute to perform the request.

To create another category, a child of the previous

::

    {
        "category_name": "Men's Fashion",
        "parent_category": 1
    }
