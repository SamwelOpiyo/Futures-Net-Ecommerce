from django.urls import path, include

from rest_framework import routers

from catalogue.api.views import (
    ProductViewSet,
    ProductCategoryViewSet,
    MediaUploadViewSet,
)


router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, "products")
router.register(
    r"product-categories", ProductCategoryViewSet, "product_categories"
)
router.register(r"media-uploads", MediaUploadViewSet, "media_uploads")


urlpatterns = [path("", include(router.urls))]
