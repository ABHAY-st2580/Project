from django.db import models


class Tile(models.Model):
    tile_id = models.AutoField(primary_key=True)
    tile_name_number = models.CharField(max_length=100, unique=True)
    tile_type = models.CharField(max_length=50)
    tile_type2 = models.CharField(max_length=10,
        null=True,
        blank=True,
        choices=[('HL','HL'), ('L','L'), ('D','D'), ('F','F'), ('AT', 'AT')])
    price_per_box = models.IntegerField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.tile_name_number} ({self.tile_type})"

