from django.contrib import admin
from .models import Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'sale_id',
        'customer_name',
        'amount',
        'remaining_amount',
        'date',
        'phone_number'
    )

    search_fields = (
        'customer_name',
        'phone_number'
    )

    list_filter = (
        'date',
    )
    inline = [SaleItemInline]
    ordering = ('-date',)

    list_per_page = 20


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = (
        'sale',
        'tile_type',
        'tile_name_number',
        'tile_type2',
        'quantity'
    )

    search_fields = (
        'tile_name_number',
        'tile_type',
        'tile_type2'
    )

    list_filter = (
        'tile_type',
        'tile_type2'
    )

    list_per_page = 20