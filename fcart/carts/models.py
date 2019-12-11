from django.db import models

# Create your models here.
class Redmi_Mobiles(models.Model):
    model_name=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    rating=models.FloatField()

    def __str__(self):
        return self.model_name