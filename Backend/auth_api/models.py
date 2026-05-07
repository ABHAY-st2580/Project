from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, default = "Not specified")
    def __str__(self):
        return f"{self.shop_name}({self.location})"


class Membership(models.Model):
    ROLE_CHOICES = [
        ('OWNER', 'Owner'),
        ('STAFF', 'Staff'),
        ('ACCOUNTANT', 'Accountant'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'shop')

    def __str__(self):
        return f"{self.user.username} - {self.shop.shop_name} ({self.role})"