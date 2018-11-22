from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy


class ProductCategoryViewSetTestCase(APITestCase):
    """
    Test suite for Product Category api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")

        self.post_data = {"category_name": "Test Category"}

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("product_categories-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_category_post(self):
        """
        Test Product Category creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            self.response.json()["category_name"], "Test Category"
        )
        self.assertEqual(self.response.json()["parent_category_details"], None)

    def test_anonymous_user_product_category_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product Category.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("product_categories-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_product_category_list(self):
        """
        Test the api endpoint for list product categories.
        """
        response = self.client.get(
            reverse("product_categories-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_category_list(self):
        """
        Test the api endpoint for list product categories using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("product_categories-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_product_category_retrieve(self):
        """
        Test the api endpoint for retrieve product category.
        """
        new_product_category = mommy.make("catalogue.ProductCategory")
        response = self.client.get(
            reverse(
                "product_categories-detail",
                args=[self.api_version, new_product_category.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_category_retrieve(self):
        """
        Test the api endpoint for retrieve product category using request from
        anonymous user.
        """
        new_client = APIClient()
        new_product_category = mommy.make("catalogue.ProductCategory")
        new_response = new_client.get(
            reverse(
                "product_categories-detail",
                args=[self.api_version, new_product_category.id],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)


class ProductViewSetTestCase(APITestCase):
    """
    Test suite for Product api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")
        self.new_product_category = mommy.make("catalogue.ProductCategory")

        self.post_data = {
            "product_name": "Test",
            "description": "Test Product",
            "product_price": 120.00,
            "product_category": self.new_product_category.id,
            "date_of_manufacture": "2018-10-22T03:17:59.727272Z",
            "expiry_date": "2020-10-22T03:17:59.727272Z",
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("products-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_post(self):
        """
        Test Product creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_product_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("products-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_product_list(self):
        """
        Test the api endpoint for list products.
        """
        response = self.client.get(
            reverse("products-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_list(self):
        """
        Test the api endpoint for list products using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("products-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_product_retrieve(self):
        """
        Test the api endpoint for retrieve product.
        """
        new_product = mommy.make("catalogue.Product")
        response = self.client.get(
            reverse(
                "products-detail", args=[self.api_version, new_product.key]
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_retrieve(self):
        """
        Test the api endpoint for retrieve product using request from
        anonymous user.
        """
        new_client = APIClient()
        new_product = mommy.make("catalogue.Product")
        new_response = new_client.get(
            reverse(
                "products-detail", args=[self.api_version, new_product.key]
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)


class AttributeGroupViewSetTestCase(APITestCase):
    """
    Test suite for Product Attribute Group api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")

        self.post_data = {"attribute_group_name": "Color"}

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("attribute_groups-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_post(self):
        """
        Test Product Attribute Group creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_attribute_group_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product Attribute Group.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("attribute_groups-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_attribute_group_list(self):
        """
        Test the api endpoint for list product attribute groups.
        """
        response = self.client.get(
            reverse("attribute_groups-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_attribute_group_list(self):
        """
        Test the api endpoint for list product attribute groups using request
        from anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("attribute_groups-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_attribute_group_retrieve(self):
        """
        Test the api endpoint for retrieve attribute group.
        """
        new_attribute_group = mommy.make("catalogue.AttributeGroup")
        response = self.client.get(
            reverse(
                "attribute_groups-detail",
                args=[self.api_version, new_attribute_group.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_attribute_group_retrieve(self):
        """
        Test the api endpoint for retrieve attribute group using request from
        anonymous user.
        """
        new_client = APIClient()
        new_attribute_group = mommy.make("catalogue.AttributeGroup")
        new_response = new_client.get(
            reverse(
                "attribute_groups-detail",
                args=[self.api_version, new_attribute_group.id],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)


class ProductAttributeViewSetTestCase(APITestCase):
    """
    Test suite for Product Attribute api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")
        self.new_attribute_group = mommy.make("catalogue.AttributeGroup")
        self.new_product = mommy.make("catalogue.Product")

        self.post_data = {
            "attribute_name": "Test Attribute",
            "attribute_group": self.new_attribute_group.id,
            "product": self.new_product.key,
            "attribute_mandatory_value_type": "text",
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("product_attributes-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_attribute_post(self):
        """
        Test Product Attribute creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_product_attribute_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product Attribute.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("product_attributes-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_product_attribute_list(self):
        """
        Test the api endpoint for list product attributes.
        """
        response = self.client.get(
            reverse("product_attributes-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_attribute_list(self):
        """
        Test the api endpoint for list product attributes using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("product_attributes-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_product_attribute_retrieve(self):
        """
        Test the api endpoint for retrieve product attribute.
        """
        new_product_attribute = mommy.make("catalogue.ProductAttribute")
        response = self.client.get(
            reverse(
                "product_attributes-detail",
                args=[self.api_version, new_product_attribute.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_attribute_retrieve(self):
        """
        Test the api endpoint for retrieve product attribute using request from
        anonymous user.
        """
        new_client = APIClient()
        new_product_attribute = mommy.make("catalogue.ProductAttribute")
        new_response = new_client.get(
            reverse(
                "product_attributes-detail",
                args=[self.api_version, new_product_attribute.id],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)


class ProductAttributeValueViewSetTestCase(APITestCase):
    """
    Test suite for Product Attribute Value api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")
        self.new_product_attribute = mommy.make("catalogue.ProductAttribute")

        self.post_data = {
            "attribute_value_text": "Test Attribute Value",
            "product_attribute": self.new_product_attribute.id,
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("product_attribute_values-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_attribute_value_post(self):
        """
        Test Product Attribute Value creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_product_attribute_value_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product Attribute Value.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("product_attribute_values-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_product_attribute_values_list(self):
        """
        Test the api endpoint for list product attribute values.
        """
        response = self.client.get(
            reverse("product_attribute_values-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_attribute_values_list(self):
        """
        Test the api endpoint for list product attribute values using request
        from anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("product_attribute_values-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_product_attribute_value_retrieve(self):
        """
        Test the api endpoint for retrieve product attribute value.
        """
        new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )
        response = self.client.get(
            reverse(
                "product_attribute_values-detail",
                args=[self.api_version, new_product_attribute_value.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_attribute_value_retrieve(self):
        """
        Test the api endpoint for retrieve product attribute value using
        request from anonymous user.
        """
        new_client = APIClient()
        new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )
        new_response = new_client.get(
            reverse(
                "product_attribute_values-detail",
                args=[self.api_version, new_product_attribute_value.id],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)


class ProductStockViewSetTestCase(APITestCase):
    """
    Test suite for Product Stock api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """

        self.api_version = "v1"
        self.new_user = mommy.make("users.User")
        self.new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )

        self.post_data = {
            "product_attribute_value": self.new_product_attribute_value.id,
            "in_store": 10,
        }

        self.client = APIClient()
        self.client.force_authenticate(user=self.new_user)
        self.response = self.client.post(
            reverse("product_stock-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )

    def test_product_stock_post(self):
        """
        Test Product Stock creation.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_product_stock_post(self):
        """
        Test if the api can raise error if anonymous user tries to create a
        Product Stock.
        """
        new_client = APIClient()
        new_response = new_client.post(
            reverse("product_stock-list", args=[self.api_version]),
            self.post_data,
            format="json",
        )
        self.assertEqual(
            new_response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_get_product_stock_list(self):
        """
        Test the api endpoint for list product stock.
        """
        response = self.client.get(
            reverse("product_stock-list", args=[self.api_version])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_stock_list(self):
        """
        Test the api endpoint for list product stock using request from
        anonymous user.
        """
        new_client = APIClient()
        new_response = new_client.get(
            reverse("product_stock-list", args=[self.api_version])
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_get_stock_retrieve(self):
        """
        Test the api endpoint for retrieve product stock.
        """
        new_product_stock = mommy.make("catalogue.ProductStock")
        response = self.client.get(
            reverse(
                "product_stock-detail",
                args=[self.api_version, new_product_stock.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_get_product_stock_retrieve(self):
        """
        Test the api endpoint for retrieve product stock using request from
        anonymous user.
        """
        new_client = APIClient()
        new_product_stock = mommy.make("catalogue.ProductStock")
        new_response = new_client.get(
            reverse(
                "product_stock-detail",
                args=[self.api_version, new_product_stock.id],
            )
        )
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
