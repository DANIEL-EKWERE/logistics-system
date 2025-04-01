from django.db import models

# Create your models here.

class Courier(models.Model):
    invoice_id = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    shipment_content_type = models.CharField(max_length=20)
    freight_type = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    city_of_departure = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.code

