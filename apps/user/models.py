from django.db import models

# Create your models here.

class Countries(models.Model):
    country_name = models.CharField(verbose_name="Nombre", max_length=250)
    nationality = models.CharField(verbose_name="Nombre", max_length=250)

class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=50, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=250)
    birth_date = models.DateField(null=True)
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, related_name="country")

