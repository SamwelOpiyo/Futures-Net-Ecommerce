from django.core.files.base import ContentFile
from django.test import TestCase

from model_mommy import mommy

from futures_net_ecommerce.users.models import User
from catalogue.models import (
    ProductAttribute,
    ProductAttributeGroup,
    MediaUpload,
    ProductCategory,
    Product,
    ProductStock,
    ProductAttributeValue,
)

# Create your tests here.


class TestProductCategoryModel(TestCase):
    """
    Test Product Category creation using data generated by model_mommy
    """

    def setUp(self):
        self.new_product_category = mommy.make("catalogue.ProductCategory")

    def test_product_category_creation_mommy(self):
        self.assertTrue(isinstance(self.new_product_category, ProductCategory))
        self.assertTrue(self.new_product_category.__str__(), self.new_product_category.category_slug)


class TestMediaUploadModel(TestCase):
    """
    Test Media creation using data generated by model_mommy
    """

    def setUp(self):
        self.new_user = mommy.make("users.User")
        self.new_media = mommy.make("catalogue.MediaUpload", media_file=ContentFile('A string with the file content'))

    def test_media_creation_mommy(self):
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_media, MediaUpload))
        self.assertTrue(self.new_media.__str__(), self.new_media.media_key)


class TestProductModel(TestCase):
    """
    Test Product creation using data generated by model_mommy
    """

    def setUp(self):
        self.new_user = mommy.make("users.User")
        self.new_product = mommy.make("catalogue.Product")

    def test_product_creation_mommy(self):
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_product, Product))
        self.assertTrue(self.new_product.__str__(), self.new_product.product_slug)


class TestProductAttributeGroupModel(TestCase):
    """
    Test Product Attribute Group creation using generated data by model_mommy
    """

    def setUp(self):
        self.new_product_attribute_group = mommy.make(
            "catalogue.ProductAttributeGroup"
        )

    def test_product_attribute_group_creation_mommy(self):
        self.assertTrue(
            isinstance(self.new_product_attribute_group, ProductAttributeGroup)
        )
        self.assertTrue(self.new_product_attribute_group.__str__(), self.new_product_attribute_group.attribute_group_name)


class TestProductAttributeModel(TestCase):
    """
    Test Product Attribute creation using generated data by model_mommy
    """

    def setUp(self):
        self.new_product = mommy.make("catalogue.Product")
        self.new_product_attribute = mommy.make("catalogue.ProductAttribute")

    def test_product_attribute_creation_mommy(self):
        self.assertTrue(isinstance(self.new_product, Product))
        self.assertTrue(self.new_product.__str__(), self.new_product.product_slug)
        self.assertTrue(isinstance(self.new_product_attribute, ProductAttribute))
        self.assertTrue(self.new_product_attribute.__str__(), self.new_product_attribute.attribute_name)


class TestProductAttributeValueModel(TestCase):
    """
    Test Product Attribute Value creation using generated data by model_mommy
    """

    def setUp(self):
        self.new_product_attribute = mommy.make("catalogue.ProductAttribute")
        self.new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )

    def test_product_attribute_value_creation_mommy(self):
        self.assertTrue(isinstance(self.new_product_attribute, ProductAttribute))
        self.assertTrue(self.new_product_attribute.__str__(), self.new_product_attribute.attribute_name)
        self.assertTrue(
            isinstance(self.new_product_attribute_value, ProductAttributeValue)
        )
        self.assertTrue(self.new_product_attribute_value.__str__(), self.new_product_attribute_value.product_attribute.attribute_name)


class TestProductStockModel(TestCase):
    """
    Test Product Stock creation using data generated by model_mommy
    """

    def setUp(self):
        self.new_product = mommy.make("catalogue.Product")
        self.new_product_stock = mommy.make("catalogue.ProductStock")

    def test_product_stock_creation_mommy(self):
        self.assertTrue(isinstance(self.new_product, Product))
        self.assertTrue(self.new_product.__str__(), self.new_product.product_slug)
        self.assertTrue(isinstance(self.new_product_stock, ProductStock))
        self.assertTrue(self.new_product_stock.__str__(), self.new_product_stock.product.product_slug)