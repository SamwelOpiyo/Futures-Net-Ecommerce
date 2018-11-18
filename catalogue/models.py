from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from uuid import uuid4

from catalogue.utils import get_upload_media_name
from futures_net_ecommerce.users.models import User

# Create your models here.


class MandatoryFieldsModel(models.Model):
    """
    Parent Class for all models to add created and edited date fields.
    """

    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created")
    )
    updated = models.DateTimeField(
        db_index=True, auto_now=True, verbose_name=_("last updated")
    )

    class Meta:
        indexes = (BrinIndex(fields=["created"]),)
        ordering = ["-created"]
        abstract = True


class ProductCategory(MandatoryFieldsModel):
    category_name = models.CharField(
        max_length=100, verbose_name=_("product category name")
    )
    parent_category = models.ForeignKey(
        "ProductCategory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_("parent product category"),
    )
    category_slug = models.SlugField(
        max_length=100, verbose_name=_("product category slug")
    )

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_slug


class MediaUpload(MandatoryFieldsModel):

    MEDIA_UPLOAD_TYPES = (
        ("image", "Image File"),
        ("audio", "Audio File"),
        ("video", "Video File"),
        ("other", "Other File"),
    )

    media_key = models.UUIDField(
        default=uuid4,
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name=_("media upload key"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="id", verbose_name=_("user"), db_index=True
    )
    media_type = models.CharField(
        max_length=5,
        choices=MEDIA_UPLOAD_TYPES,
        default="image",
        blank=True,
        verbose_name=_("media upload type"),
    )
    media_file = models.FileField(
        upload_to=get_upload_media_name,
        verbose_name=_("media upload file"),
    )
    media_upload_thumbnail = models.ManyToManyField(
        "self",
        related_name="media_file_thumbnail",
        blank=True,
        symmetrical=False,
        verbose_name=_("media upload thumbnail"),
    )

    class Meta:
        verbose_name = _("media upload")
        verbose_name_plural = _("media uploads")

    def __str__(self):
        return str(self.media_key)


class Product(MandatoryFieldsModel):

    key = models.UUIDField(
        default=uuid4,
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name=_("product key"),
    )
    product_name = models.CharField(
        max_length=100, verbose_name=_("product name")
    )
    date_of_manufacture = models.DateTimeField(
        blank=True, null=True, verbose_name=_("product date of manufacture")
    )
    expiry_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_("product expiry date")
    )
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="product_category",
        verbose_name=_("product category"),
        db_index=True,
    )
    publisher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_publisher",
        verbose_name=_("product publisher"),
        db_index=True,
    )
    description = models.TextField(verbose_name=_("product description"))
    product_slug = models.SlugField(
        max_length=100, verbose_name=_("product slug")
    )
    product_media_files = models.ManyToManyField(
        "MediaUpload",
        related_name="product_media_files",
        blank=True,
        verbose_name=_("product media files"),
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_slug


class ProductAttributeGroup(MandatoryFieldsModel):
    attribute_group_name = models.CharField(
        max_length=100, verbose_name=_("product attribute group name")
    )
    parent_attribute_group = models.ForeignKey(
        "ProductAttributeGroup",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_("parent product attribute group"),
    )

    class Meta:
        verbose_name = _("product attribute group")
        verbose_name_plural = _("product attribute groups")

    def __str__(self):
        return self.attribute_group_name


class ProductAttribute(MandatoryFieldsModel):

    PRODUCT_ATTRIBUTE_VALUE_TYPES = (
        ("integer", _("Integer")),
        ("text", _("Text")),
        ("boolean", _("Boolean")),
        ("float", _("Float")),
        ("datetime", _("Datetime")),
        ("date", _("Date")),
        ("object", _("Model Object")),
    )
    attribute_name = models.CharField(
        max_length=100, verbose_name=_("product attribute name")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name=_("product"),
        db_index=True,
    )
    attribute_mandatory_value_type = models.CharField(
        max_length=5,
        choices=PRODUCT_ATTRIBUTE_VALUE_TYPES,
        default="text",
        verbose_name=_("product attribute value type"),
    )
    attribute_group = models.ForeignKey(
        "ProductAttributeGroup",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_("product attribute group"),
    )

    class Meta:
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")

    def __str__(self):
        return self.attribute_name


class ProductAttributeValue(MandatoryFieldsModel):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.CASCADE,
        related_name="product_attribute",
        verbose_name=_("product attribute"),
        db_index=True,
    )
    additional_price = models.DecimalField(
        max_digits=12, decimal_places=3, verbose_name=_("rating")
    )
    attribute_value_text = models.TextField(
        blank=True, null=True, verbose_name=_("product attribute text value")
    )
    attribute_value_integer = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("product attribute integer value"),
    )
    attribute_value_boolean = models.NullBooleanField(
        blank=True, verbose_name=_("product attribute boolean value")
    )
    attribute_value_float = models.FloatField(
        blank=True, null=True, verbose_name=_("product attribute float value")
    )
    attribute_value_date = models.DateField(
        blank=True, null=True, verbose_name=_("product attribute date value")
    )
    attribute_value_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("product attribute datetime value"),
    )
    attribute_value_object = GenericForeignKey(
        "object_content_type",
        "object_id",
    )

    object_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("product attribute object content type"),
    )
    object_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_("product attribute object ID")
    )

    class Meta:
        verbose_name = _("product attribute value")
        verbose_name_plural = _("product attribute values")

    def __str__(self):
        return self.product_attribute.attribute_name


class ProductStock(MandatoryFieldsModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="stock_product",
        verbose_name=_("product"),
        db_index=True,
    )
    in_store = models.PositiveSmallIntegerField(
        verbose_name=_("products in store")
    )
    sold = models.PositiveSmallIntegerField(verbose_name=_("products sold"))

    class Meta:
        verbose_name = _("product stock")
        verbose_name_plural = _("product stock")

    def __str__(self):
        return self.product.product_slug
