from django.db import models

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    remaining_amount = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Sale {self.sale_id} - {self.customer_name}"



class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')

    tile_type = models.CharField(max_length=50)
    tile_name_number = models.CharField(max_length=100)

    tile_type2 = models.CharField(
        max_length=10,
        default='AT',
        blank=True,
        choices=[('HL','HL'), ('L','L'), ('D','D'), ('F','F'), ('AT', 'AT')]
    )

    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.tile_type} - {self.tile_name_number} ({self.quantity})"