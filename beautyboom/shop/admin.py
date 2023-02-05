from django.contrib import admin

from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'parent', 'slug', 'icon']
    prepopulated_fields = {'slug': ('tittle',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created',
                    'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available', 'category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
