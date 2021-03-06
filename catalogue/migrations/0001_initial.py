# Generated by Django 2.0.9 on 2018-11-22 16:11

import catalogue.utils
from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AttributeGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "attribute_group_name",
                    models.CharField(
                        max_length=100,
                        verbose_name="product attribute group name",
                    ),
                ),
                (
                    "parent_attribute_group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.AttributeGroup",
                        verbose_name="parent product attribute group",
                    ),
                ),
            ],
            options={
                "verbose_name": "product attribute group",
                "verbose_name_plural": "product attribute groups",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="MediaUpload",
            fields=[
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "media_key",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="media upload key",
                    ),
                ),
                (
                    "media_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("image", "Image File"),
                            ("audio", "Audio File"),
                            ("video", "Video File"),
                            ("other", "Other File"),
                        ],
                        default="image",
                        max_length=5,
                        verbose_name="media upload type",
                    ),
                ),
                (
                    "media_file",
                    models.FileField(
                        upload_to=catalogue.utils.get_upload_media_name,
                        verbose_name="media upload file",
                    ),
                ),
                (
                    "media_upload_thumbnail",
                    models.ManyToManyField(
                        blank=True,
                        related_name="media_file_thumbnail",
                        to="catalogue.MediaUpload",
                        verbose_name="media upload thumbnail",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "media upload",
                "verbose_name_plural": "media uploads",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "key",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="product key",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(
                        max_length=100, verbose_name="product name"
                    ),
                ),
                (
                    "date_of_manufacture",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="product date of manufacture",
                    ),
                ),
                (
                    "expiry_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="product expiry date",
                    ),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        decimal_places=3,
                        max_digits=13,
                        verbose_name="product_price",
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="product description"),
                ),
                (
                    "product_slug",
                    models.SlugField(
                        max_length=100, verbose_name="product slug"
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "attribute_name",
                    models.CharField(
                        max_length=100, verbose_name="product attribute name"
                    ),
                ),
                (
                    "attribute_mandatory_value_type",
                    models.CharField(
                        choices=[
                            ("integer", "Integer"),
                            ("text", "Text"),
                            ("boolean", "Boolean"),
                            ("float", "Float"),
                            ("datetime", "Datetime"),
                            ("date", "Date"),
                            ("object", "Model Object"),
                        ],
                        default="text",
                        max_length=5,
                        verbose_name="product attribute value type",
                    ),
                ),
                (
                    "attribute_group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.AttributeGroup",
                        verbose_name="product attribute group",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="catalogue.Product",
                        verbose_name="product",
                    ),
                ),
            ],
            options={
                "verbose_name": "product attribute",
                "verbose_name_plural": "product attributes",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "additional_price",
                    models.DecimalField(
                        decimal_places=3,
                        default=0.0,
                        max_digits=12,
                        verbose_name="additional_price",
                    ),
                ),
                (
                    "attribute_value_text",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute text value",
                    ),
                ),
                (
                    "attribute_value_integer",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute integer value",
                    ),
                ),
                (
                    "attribute_value_boolean",
                    models.NullBooleanField(
                        verbose_name="product attribute boolean value"
                    ),
                ),
                (
                    "attribute_value_float",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute float value",
                    ),
                ),
                (
                    "attribute_value_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute date value",
                    ),
                ),
                (
                    "attribute_value_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute datetime value",
                    ),
                ),
                (
                    "object_id",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="product attribute object ID",
                    ),
                ),
                (
                    "object_content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                        verbose_name="product attribute object content type",
                    ),
                ),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_attribute",
                        to="catalogue.ProductAttribute",
                        verbose_name="product attribute",
                    ),
                ),
            ],
            options={
                "verbose_name": "product attribute value",
                "verbose_name_plural": "product attribute values",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        max_length=100, verbose_name="product category name"
                    ),
                ),
                (
                    "category_slug",
                    models.SlugField(
                        max_length=100, verbose_name="product category slug"
                    ),
                ),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.ProductCategory",
                        verbose_name="parent product category",
                    ),
                ),
            ],
            options={
                "verbose_name": "product category",
                "verbose_name_plural": "product categories",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="ProductStock",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        db_index=True,
                        verbose_name="last updated",
                    ),
                ),
                (
                    "in_store",
                    models.PositiveSmallIntegerField(
                        verbose_name="products in store"
                    ),
                ),
                (
                    "sold",
                    models.PositiveSmallIntegerField(
                        verbose_name="products sold"
                    ),
                ),
                (
                    "product_attribute_value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock_product_attribute_value",
                        to="catalogue.ProductAttributeValue",
                        verbose_name="Stock of Specific Value of the Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "product stock",
                "verbose_name_plural": "product stock",
                "ordering": ["-created"],
            },
        ),
        migrations.AddField(
            model_name="product",
            name="product_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_category",
                to="catalogue.ProductCategory",
                verbose_name="product category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_media_files",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_media_files",
                to="catalogue.MediaUpload",
                verbose_name="product media files",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_publisher",
                to=settings.AUTH_USER_MODEL,
                verbose_name="product publisher",
            ),
        ),
        migrations.AddIndex(
            model_name="productstock",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_p_created_7043ff_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="productcategory",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_p_created_f5cbbe_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="productattributevalue",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_p_created_de4f59_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="productattribute",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_p_created_4c0a51_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_p_created_9dc884_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="mediaupload",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_m_created_33c05d_brin"
            ),
        ),
        migrations.AddIndex(
            model_name="attributegroup",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="catalogue_a_created_305990_brin"
            ),
        ),
    ]
