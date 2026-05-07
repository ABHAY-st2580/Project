from django.contrib import admin
from .models import Tile


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = (
        'tile_name_number',
        'tile_type',
        'tile_type2',
        'price_per_box',
        'stock_quantity'
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

    ordering = ('tile_name_number',)