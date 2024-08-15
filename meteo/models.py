from django.db import models


class Worldcities(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)
    city = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worldcities'

# Create your models here.
