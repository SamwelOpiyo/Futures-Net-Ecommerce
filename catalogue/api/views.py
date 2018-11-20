from rest_framework import views, viewsets

from catalogue.models import Product, ProductCategory, MediaUpload
from catalogue.api.serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    MediaUploadSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Products.
    """

    queryset = Product.objects.select_related(
        "product_category", "publisher"
    ).prefetch_related(
        "product_media_files__user",
        "product_media_files__media_upload_thumbnail",
        "product_category__parent_category",
    )
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff will be able to create a Product.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.validated_data["publisher"] = self.request.user
                serializer.save()

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.validated_data["publisher"] = self.request.user
                serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                instance.delete()


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Product Categories.
    """

    queryset = ProductCategory.objects.select_related("parent_category")
    serializer_class = ProductCategorySerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff will be able to create product category.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.save()

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                instance.delete()


class MediaUploadViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Media Uploads.
    """

    queryset = MediaUpload.objects.select_related("user").prefetch_related(
        "media_upload_thumbnail"
    )
    serializer_class = MediaUploadSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff will be able to create product category.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.validated_data["user"] = self.request.user
                serializer.save()

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                serializer.validated_data["user"] = self.request.user
                serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                instance.delete()
