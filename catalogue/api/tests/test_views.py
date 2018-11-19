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
