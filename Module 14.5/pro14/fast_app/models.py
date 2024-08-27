from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    big_integer_field = models.BigIntegerField()
    dUration=models.DurationField()
    image_field = models.ImageField(upload_to='images/')
    slug_field = models.SlugField()
    uuid_field = models.UUIDField()
    positive_integer_field = models.PositiveIntegerField()
    