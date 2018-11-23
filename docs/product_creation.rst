Creating a Product
==================

Using Swagger API Docs
----------------------

Click on API to Extend it.

* When creating any request, remember to always set version to v1.

Create Product Category
^^^^^^^^^^^^^^^^^^^^^^^

Extend ``POST - /api/{version}/product-categories/``

Click Try it out.

Fill in version with v1.

Input the following json data.

::

    {
        "category_name": "Fashion"
    }

then click on execute to perform the request. Obtain the id in the response for the next request.

To create another category, a child of the previous:

::

    {
        "category_name": "Men's Fashion",
        "parent_category": 1
    }


Upload MediaFiles
^^^^^^^^^^^^^^^^^

Upload Product Files such as Images at `http://127.0.0.1:8000/api/v1/media-uploads/ <http://127.0.0.1:8000/api/v1/media-uploads/>`_. Obtain the media file keys for the request below.


Create Product
^^^^^^^^^^^^^^

Extend ``POST - /api/{version}/products/``


Click Try it out.

Fill in version with v1.

Input the following json data.

::

    {
        "product_name": "BMW Khaki Men's Trousers",
        "description": "Quality Men's trouser by BMW.",
        "product_price": 1500,
        "product_category": 2,
        "product_media_files": [
            "5dd25fa4-0b6a-4559-85dc-a67499d508d8",
            "53fe7d50-236c-4c63-b888-eee1f68dc0f8"
        ]
    }

then click on execute to perform the request. Obtain the key in the response for the following requests.


Create Attribute Groups
^^^^^^^^^^^^^^^^^^^^^^^

Extend ``POST - /api/{version}/attribute-groups/``

Click Try it out.

Fill in version with v1.

Input the following json data.

::

    {
        "attribute_group_name": "Shipped From Kenya"
    }

then click on execute to perform the request. Obtain the id in the response for the next request.

To create another category, a child of the previous

{
  "attribute_group_name": "Size",
  "parent_attribute_group": 1
}

then click on execute to perform the request. Obtain the id in the response for the next request.

To create other categories, children of the previous do the same for:

::

    {
        "attribute_group_name": "XXL",
        "parent_attribute_group": 2
    }

::

    {
        "attribute_group_name": "XL",
        "parent_attribute_group": 2
    }

::

    {
        "attribute_group_name": "L",
        "parent_attribute_group": 2
    }


Create Product Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

Extend ``POST - /api/{version}/product-attributes/``

Click Try it out.

Fill in version with v1.

Input the following json data to create variation of XXL Size.

::

    {
      "attribute_name": "Color",
      "product": "4eabb237-ce89-46a5-92f2-bdc55873f708",
      "attribute_mandatory_value_type": "text",
      "attribute_group": 3
    }

then click on execute to perform the request. Do the same for XL and L.

::

    {
      "attribute_name": "Color",
      "product": "4eabb237-ce89-46a5-92f2-bdc55873f708",
      "attribute_mandatory_value_type": "text",
      "attribute_group": 4
    }

::

    {
      "attribute_name": "Color",
      "product": "4eabb237-ce89-46a5-92f2-bdc55873f708",
      "attribute_mandatory_value_type": "text",
      "attribute_group": 5
    }


Create Product Attribute Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extend ``POST - /api/{version}/product-attribute-values/``

Click Try it out.

Fill in version with v1.

Input the following json data to create values for color variation of XXL.

::

    {
      "product_attribute": 1,
      "attribute_value_text": "Blue"
    }

then click on execute to perform the request. Add another for same product attribute. Get the product attribute value ids for requests below.

::

    {
      "product_attribute": 1,
      "attribute_value_text": "Pink"
    }

Add more more records for color variations of XL and L.

::

    {
      "product_attribute": 2,
      "attribute_value_text": "Blue"
    }

::

    {
      "product_attribute": 2,
      "attribute_value_text": "Maroon"
    }

::

    {
      "product_attribute": 3,
      "attribute_value_text": "Grey"
    }

::

    {
      "product_attribute": 3,
      "attribute_value_text": "Maroon"
    }


Create Product Stock According to ProductAttribute Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extend ``POST - http://127.0.0.1:8000/api/v1/product-stock/``

Click Try it out.

Fill in version with v1.

Input the following json data to create product stock values for each sub-variation of product.

::

    {
      "product_attribute_value": 1,
      "in_store": 10
    }

::

    {
      "product_attribute_value": 2,
      "in_store": 15
    }

::

    {
      "product_attribute_value": 3,
      "in_store": 13
    }

::

    {
      "product_attribute_value": 4,
      "in_store": 19
    }

::

    {
      "product_attribute_value": 5,
      "in_store": 17
    }

::

    {
      "product_attribute_value": 6,
      "in_store": 15
    }

Final Product
-------------

::

    {
        "key": "17dc52cc-ed85-4566-98a6-b4d5ed747fdf",
        "product_name": "BMW Khaki Men's Trousers",
        "description": "Quality Men's trouser by BMW.",
        "product_price": "1500.000",
        "product_category_details": {
            "id": 2,
            "category_name": "Men's Fashion",
            "category_slug": "mens-fashion",
            "parent_category_details": {
                "id": 1,
                "category_name": "Fashion",
                "category_slug": "fashion",
                "parent_category_details": null
            }
        },
        "product_slug": "bmw-khaki-mens-trousers",
        "product_media_files_details": [
            {
                "media_key": "8dc5da3d-8311-488d-a245-549df44f8a78",
                "user": "SamwelOpiyo",
                "media_type": "image",
                "media_file": "/media/media/images/8dc5da3d-8311-488d-a245-549df44f8a78.jpeg",
                "media_upload_thumbnail_details": []
            },
            {
                "media_key": "2aa681b9-e690-4142-ad08-94c2e39acc93",
                "user": "SamwelOpiyo",
                "media_type": "image",
                "media_file": "/media/media/images/2aa681b9-e690-4142-ad08-94c2e39acc93.png",
                "media_upload_thumbnail_details": []
            }
        ],
        "product_attributes_details": [
            {
                "id": 3,
                "attribute_name": "Color",
                "product_name": "BMW Khaki Men's Trousers",
                "attribute_mandatory_value_type": "text",
                "attribute_group_details": {
                    "id": 5,
                    "attribute_group_name": "L",
                    "parent_attribute_group_details": {
                        "id": 2,
                        "attribute_group_name": "Size",
                        "parent_attribute_group_details": {
                            "id": 1,
                            "attribute_group_name": "Shipped From Kenya",
                            "parent_attribute_group_details": null
                        }
                    }
                },
                "attribute_values_details": [
                    {
                        "id": 6,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 6,
                            "product_attribute_value": 6,
                            "product_attribute_text": "Maroon",
                            "in_store": 15,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Maroon"
                            }
                        ],
                        "attribute_value_object": null
                    },
                    {
                        "id": 5,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 5,
                            "product_attribute_value": 5,
                            "product_attribute_text": "Grey",
                            "in_store": 17,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Grey"
                            }
                        ],
                        "attribute_value_object": null
                    }
                ]
            },
            {
                "id": 2,
                "attribute_name": "Color",
                "product_name": "BMW Khaki Men's Trousers",
                "attribute_mandatory_value_type": "text",
                "attribute_group_details": {
                    "id": 4,
                    "attribute_group_name": "XL",
                    "parent_attribute_group_details": {
                        "id": 2,
                        "attribute_group_name": "Size",
                        "parent_attribute_group_details": {
                            "id": 1,
                            "attribute_group_name": "Shipped From Kenya",
                            "parent_attribute_group_details": null
                        }
                    }
                },
                "attribute_values_details": [
                    {
                        "id": 4,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 4,
                            "product_attribute_value": 4,
                            "product_attribute_text": "Maroon",
                            "in_store": 19,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Maroon"
                            }
                        ],
                        "attribute_value_object": null
                    },
                    {
                        "id": 3,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 3,
                            "product_attribute_value": 3,
                            "product_attribute_text": "Blue",
                            "in_store": 13,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Blue"
                            }
                        ],
                        "attribute_value_object": null
                    }
                ]
            },
            {
                "id": 1,
                "attribute_name": "Color",
                "product_name": "BMW Khaki Men's Trousers",
                "attribute_mandatory_value_type": "text",
                "attribute_group_details": {
                    "id": 3,
                    "attribute_group_name": "XXL",
                    "parent_attribute_group_details": {
                        "id": 2,
                        "attribute_group_name": "Size",
                        "parent_attribute_group_details": {
                            "id": 1,
                            "attribute_group_name": "Shipped From Kenya",
                            "parent_attribute_group_details": null
                        }
                    }
                },
                "attribute_values_details": [
                    {
                        "id": 2,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 2,
                            "product_attribute_value": 2,
                            "product_attribute_text": "Pink",
                            "in_store": 15,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Pink"
                            }
                        ],
                        "attribute_value_object": null
                    },
                    {
                        "id": 1,
                        "product_attribute_name": "Color",
                        "additional_price": "0.000",
                        "stock_details": {
                            "id": 1,
                            "product_attribute_value": 1,
                            "product_attribute_text": "Blue",
                            "in_store": 10,
                            "sold": 0
                        },
                        "attribute_value": [
                            {
                                "Type": "text",
                                "Value": "Blue"
                            }
                        ],
                        "attribute_value_object": null
                    }
                ]
            }
        ],
        "date_of_manufacture": null,
        "expiry_date": null,
        "publisher": "SamwelOpiyo"
    }
