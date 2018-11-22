from django.test import TestCase

from model_mommy import mommy

from catalogue.models import (
    ProductAttribute,
    AttributeGroup,
    ProductCategory,
    Product,
    ProductStock,
    ProductAttributeValue,
)
from catalogue.api.serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    AttributeGroupSerializer,
    ProductAttributeSerializer,
    ProductAttributeValueSerializer,
    ProductStockSerializer,
)


class TestProductCategorySerializer(TestCase):
    def setUp(self):
        self.new_product_category = mommy.make("catalogue.ProductCategory")
        self.another_new_product_category = mommy.make(
            "catalogue.ProductCategory"
        )

    def test_serialization_list(self):
        queryset = ProductCategory.objects.all()
        self.assertTrue(
            isinstance(
                ProductCategorySerializer(queryset, many=True).data, list
            )
        )


class TestProductSerializer(TestCase):
    def setUp(self):
        self.new_product = mommy.make("catalogue.Product")
        self.another_new_product = mommy.make("catalogue.Product")

    def test_serialization_list(self):
        queryset = Product.objects.all()
        self.assertTrue(
            isinstance(ProductSerializer(queryset, many=True).data, list)
        )


class TestAttributeGroupSerializer(TestCase):
    def setUp(self):
        self.new_attribute_group = mommy.make("catalogue.AttributeGroup")
        self.another_new_attribute_group = mommy.make(
            "catalogue.AttributeGroup"
        )

    def test_serialization_list(self):
        queryset = AttributeGroup.objects.all()
        self.assertTrue(
            isinstance(
                AttributeGroupSerializer(queryset, many=True).data, list
            )
        )


class TestProductAttributeSerializer(TestCase):
    def setUp(self):
        self.new_product_attribute = mommy.make("catalogue.ProductAttribute")
        self.another_new_product_attribute = mommy.make(
            "catalogue.ProductAttribute"
        )

    def test_serialization_list(self):
        queryset = ProductAttribute.objects.all()
        self.assertTrue(
            isinstance(
                ProductAttributeSerializer(queryset, many=True).data, list
            )
        )


class TestProductAttributeValueSerializer(TestCase):
    def setUp(self):
        self.new_product_attribute = mommy.make("catalogue.ProductAttribute")
        self.new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )
        self.another_new_product_attribute_value = mommy.make(
            "catalogue.ProductAttributeValue"
        )

    def test_serialization_list(self):
        queryset = ProductAttributeValue.objects.all()
        self.assertTrue(
            isinstance(
                ProductAttributeValueSerializer(queryset, many=True).data, list
            )
        )


class TestProductStockSerializer(TestCase):
    def setUp(self):
        self.new_product_stock = mommy.make("catalogue.ProductStock")
        self.another_new_product_stock = mommy.make("catalogue.ProductStock")

    def test_serialization_list(self):
        queryset = ProductStock.objects.all()
        self.assertTrue(
            isinstance(ProductStockSerializer(queryset, many=True).data, list)
        )
