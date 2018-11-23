from rest_framework import viewsets

from catalogue.models import (
    Product,
    ProductCategory,
    MediaUpload,
    AttributeGroup,
    ProductAttribute,
    ProductAttributeValue,
    ProductStock,
)
from catalogue.api.serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    MediaUploadSerializer,
    AttributeGroupSerializer,
    ProductAttributeSerializer,
    ProductAttributeValueSerializer,
    ProductStockSerializer,
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
        "product__attribute_group__parent_attribute_group",
        "product__product_attribute__stock_product_attribute_value",
        "product__product_attribute__attribute_value_object",
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
                serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            # Only the admins and staff members can edit.
            if self.request.user.is_superuser or self.request.user.is_staff:
                instance.delete()


class AttributeGroupViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Product Attribute Groups.
    """

    queryset = AttributeGroup.objects.select_related("parent_attribute_group")
    serializer_class = AttributeGroupSerializer

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


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Product Attributes.
    """

    queryset = ProductAttribute.objects.select_related(
        "attribute_group", "product",
    ).prefetch_related("product_attribute")
    serializer_class = ProductAttributeSerializer

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


class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Product Attribute Values.
    """

    queryset = ProductAttributeValue.objects.select_related(
        "product_attribute", "object_content_type"
    ).prefetch_related("attribute_value_object","stock_product_attribute_value")
    serializer_class = ProductAttributeValueSerializer

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


class ProductStockViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Product Stock.
    """

    queryset = ProductStock.objects.select_related("product_attribute_value")
    serializer_class = ProductStockSerializer

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
