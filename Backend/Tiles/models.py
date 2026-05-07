from django.db import models
from auth_api.models import Shop

class Tile(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    tile_id = models.AutoField(primary_key=True)
    tile_name_number = models.CharField(max_length=100)
    tile_type = models.CharField(max_length=50)
    tile_type2 = models.CharField(max_length=10,
        null=True,
        blank=True,
        choices=[('HL','HL'), ('L','L'), ('D','D'), ('F','F'), ('AT', 'AT')])
    price_per_box = models.IntegerField()
    stock_quantity = models.IntegerField()

    class Meta:
        unique_together = ('tile_type', 'tile_type2', 'tile_name_number')
    def __str__(self):
        return f"{self.tile_name_number} ({self.tile_type} - {self.tile_type2})"

