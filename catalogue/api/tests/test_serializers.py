from django.test import TestCase

from model_mommy import mommy

from catalogue.models import (
    ProductAttribute,
    ProductAttributeGroup,
    MediaUpload,
    ProductCategory,
    Product,
    ProductStock,
    ProductAttributeValue,
)
from catalogue.api.serializers import (
    ProductSerializer,
    ProductCategorySerializer,
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
