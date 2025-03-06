from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'middle_name', 'telegram_id', 'email',
                    'address', 'postal_code', 'city', 'paid', 'delivered',
                    'created', 'updated']
    list_filter = ['paid', 'delivered', 'created', 'updated']
    list_editable = ['paid', 'delivered']  # Добавляем возможность редактирования статуса доставки и оплаты
    inlines = [OrderItemInLine]