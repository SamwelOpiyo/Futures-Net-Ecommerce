from rest_framework import serializers

from catalogue.models import Product, ProductCategory, MediaUpload


class ProductCategorySerializer(serializers.ModelSerializer):
    parent_category_details = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "category_name",
            "parent_category",
            "category_slug",
            "parent_category_details",
        ]
        extra_kwargs = {
            "category_slug": {"read_only": True},
            "parent_category": {"write_only": True},
        }

    def get_parent_category_details(self, instance):
        try:
            if instance.parent_category_id:
                return ProductCategorySerializer(instance.parent_category).data
            else:
                return None
        except AttributeError:
            return None


class MediaUploadSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    media_upload_thumbnail_details = serializers.SerializerMethodField()

    class Meta:
        model = MediaUpload
        fields = [
            "media_key",
            "user",
            "media_type",
            "media_file",
            "media_upload_thumbnail_details",
        ]

    def get_user(self, instance):
        return instance.user.username

    def get_media_upload_thumbnail_details(self, instance):
        try:
            return MediaUploadSerializer(
                instance.media_upload_thumbnail.all(), many=True
            ).data
        except AttributeError:
            return None


class ProductSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField()
    product_category_details = serializers.SerializerMethodField()
    product_media_files_details = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "key",
            "product_name",
            "description",
            "product_category",
            "product_category_details",
            "product_slug",
            "product_media_files",
            "product_media_files_details",
            "date_of_manufacture",
            "expiry_date",
            "publisher",
        ]
        extra_kwargs = {
            "product_slug": {"read_only": True},
            "product_media_files": {"write_only": True},
        }

    def get_publisher(self, instance):
        try:
            return instance.publisher.username
        except AttributeError:
            return None

    def get_product_category_details(self, instance):
        try:
            if instance.product_category_id:
                return ProductCategorySerializer(
                    instance.product_category
                ).data
            else:
                return None
        except AttributeError:
            return None

    def get_product_media_files_details(self, instance):
        try:
            return MediaUploadSerializer(
                instance.product_media_files.all(), many=True
            ).data
        except AttributeError:
            return None
