from django.contrib import admin

from catalogue.models import (
    ProductAttribute,
    ProductAttributeGroup,
    MediaUpload,
    ProductCategory,
    Product,
    ProductStock,
    ProductAttributeValue,
)
# Register your models here.

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeGroup)
class ProductAttributeGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(MediaUpload)
class MediaUploadAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass
