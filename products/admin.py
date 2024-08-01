from django.contrib import admin
from django.contrib.admin import register
from products.models import Product, Category, ProductImage


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['description']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'upc', 'stock', 'category_id', 'is_active']
    search_fields = ['name', 'upc', 'price']
    list_max_show_all = 100
    inlines = [ProductImageInline]
    list_filter = ['is_active', 'category_id']
    list_editable = ['is_active']



@register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']
