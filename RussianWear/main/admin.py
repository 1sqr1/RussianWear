from django.contrib import admin
from .models import Product, Category, Size

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price',
                    'available', 'created', 'updated',
                    'discount']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['sizes']  # Добавляем возможность выбора размеров