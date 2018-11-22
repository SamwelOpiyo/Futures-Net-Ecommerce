from django.urls import path, include

from rest_framework import routers

from catalogue.api.views import (
    ProductViewSet,
    ProductCategoryViewSet,
    MediaUploadViewSet,
    AttributeGroupViewSet,
    ProductAttributeViewSet,
    ProductAttributeValueViewSet,
    ProductStockViewSet,
)


router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, "products")
router.register(
    r"product-categories", ProductCategoryViewSet, "product_categories"
)
router.register(r"media-uploads", MediaUploadViewSet, "media_uploads")
router.register(r"attribute-groups", AttributeGroupViewSet, "attribute_groups")
router.register(
    r"product-attributes", ProductAttributeViewSet, "product_attributes"
)
router.register(
    r"product-attribute-values",
    ProductAttributeValueViewSet,
    "product_attribute_values",
)
router.register(r"product-stock", ProductStockViewSet, "product_stock")


urlpatterns = [path("", include(router.urls))]
