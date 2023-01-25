from django.contrib import admin
from .models import Product, ProductsImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','publish_time']


# admin.site.register(Product)
admin.site.register(ProductsImage)
