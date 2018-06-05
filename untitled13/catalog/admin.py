
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'old_price', 'stock', 'category', 'created_at', 'Last_updated_at', 'available']
    list_filter = ['available', 'created_at', 'Last_updated_at', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


