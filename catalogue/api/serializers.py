from rest_framework import serializers

from catalogue.models import (
    Product,
    ProductCategory,
    MediaUpload,
    AttributeGroup,
    ProductAttribute,
    ProductAttributeValue,
    ProductStock,
)


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
    product_attributes_details = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "key",
            "product_name",
            "description",
            "product_price",
            "product_category",
            "product_category_details",
            "product_slug",
            "product_media_files",
            "product_media_files_details",
            "product_attributes_details",
            "date_of_manufacture",
            "expiry_date",
            "publisher",
        ]
        extra_kwargs = {
            "product_slug": {"read_only": True},
            "product_category": {"write_only": True},
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

    def get_product_attributes_details(self, instance):
        try:
            return ProductAttributeSerializer(instance.product, many=True).data
        except AttributeError:
            return None


class AttributeGroupSerializer(serializers.ModelSerializer):
    parent_attribute_group_details = serializers.SerializerMethodField()

    class Meta:
        model = AttributeGroup
        fields = [
            "id",
            "attribute_group_name",
            "parent_attribute_group",
            "parent_attribute_group_details",
        ]
        extra_kwargs = {"parent_attribute_group": {"write_only": True}}

    def get_parent_attribute_group_details(self, instance):
        try:
            if instance.parent_attribute_group_id:
                return AttributeGroupSerializer(
                    instance.parent_attribute_group
                ).data
            else:
                return None
        except AttributeError:
            return None


class ProductAttributeSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    attribute_group_details = serializers.SerializerMethodField()
    attribute_values_details = serializers.SerializerMethodField()

    class Meta:
        model = ProductAttribute
        fields = [
            "id",
            "attribute_name",
            "product",
            "product_name",
            "attribute_mandatory_value_type",
            "attribute_group",
            "attribute_group_details",
            "attribute_values_details",
        ]
        extra_kwargs = {
            "product": {"write_only": True},
            "attribute_group": {"write_only": True},
        }

    def get_product_name(self, instance):
        try:
            return instance.product.product_name
        except AttributeError:
            return None

    def get_attribute_group_details(self, instance):
        try:
            if instance.attribute_group_id:
                return AttributeGroupSerializer(instance.attribute_group).data
            else:
                return None
        except AttributeError:
            return None

    def get_attribute_values_details(self, instance):
        try:
            return ProductAttributeValueSerializer(
                instance.product_attribute, many=True
            ).data
        except AttributeError:
            return None


class GenericAttributeValueRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, MediaUpload):
            return MediaUploadSerializer(value).data
        else:
            return None


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    product_attribute_name = serializers.SerializerMethodField()
    attribute_value = serializers.SerializerMethodField()
    stock_details = serializers.SerializerMethodField()

    class Meta:
        model = ProductAttributeValue
        fields = [
            "id",
            "product_attribute",
            "product_attribute_name",
            "additional_price",
            "stock_details",
            "attribute_value",
            "attribute_value_text",
            "attribute_value_integer",
            "attribute_value_boolean",
            "attribute_value_float",
            "attribute_value_date",
            "attribute_value_datetime",
            "attribute_value_object",
        ]
        extra_kwargs = {
            "product_attribute": {"write_only": True},
            "attribute_value_text": {"write_only": True, "required": False},
            "attribute_value_integer": {"write_only": True, "required": False},
            "attribute_value_boolean": {"write_only": True, "required": False},
            "attribute_value_float": {"write_only": True, "required": False},
            "attribute_value_date": {"write_only": True, "required": False},
            "attribute_value_datetime": {
                "write_only": True,
                "required": False,
            },
            "object_content_type": {"write_only": True, "required": False},
            "object_id": {"write_only": True, "required": False},
        }

    def get_product_attribute_name(self, instance):
        try:
            return instance.product_attribute.attribute_name
        except AttributeError:
            return None

    def get_stock_details(self, instance):
        try:
            return ProductStockSerializer(
                instance.stock_product_attribute_value
            ).data
        except AttributeError:
            return None

    def get_attribute_value(self, instance):
        values = []
        try:
            if instance.attribute_value_text:
                values.append(
                    {"Type": "text", "Value": instance.attribute_value_text}
                )
        except AttributeError:
            pass
        try:
            if instance.attribute_value_integer:
                values.append(
                    {
                        "Type": "integer",
                        "Value": instance.attribute_value_integer,
                    }
                )
        except AttributeError:
            pass
        try:
            if instance.attribute_value_boolean:
                values.append(
                    {
                        "Type": "boolean",
                        "Value": instance.attribute_value_boolean,
                    }
                )
        except AttributeError:
            pass
        try:
            if instance.attribute_value_float:
                values.append(
                    {"Type": "float", "Value": instance.attribute_value_float}
                )
        except AttributeError:
            pass
        try:
            if instance.attribute_value_date:
                values.append(
                    {"Type": "date", "Value": instance.attribute_value_date}
                )
        except AttributeError:
            pass
        try:
            if instance.attribute_value_datetime:
                values.append(
                    {
                        "Type": "datetime",
                        "Value": instance.attribute_value_datetime,
                    }
                )
        except AttributeError:
            pass
        try:
            if instance.object_content_type_id:
                values.append(
                    GenericAttributeValueRelatedField(
                        instance.attribute_value_object
                    ).data
                )
        except AttributeError:
            pass
        return values


class ProductStockSerializer(serializers.ModelSerializer):
    product_attribute_text = serializers.SerializerMethodField()

    class Meta:
        model = ProductStock
        fields = [
            "id",
            "product_attribute_value",
            "product_attribute_text",
            "in_store",
            "sold",
        ]
        extra_kwargs = {"sold": {"read_only": True}}

    def get_product_attribute_text(self, instance):
        try:
            return instance.product_attribute_value.attribute_value_text
        except:
            return None
