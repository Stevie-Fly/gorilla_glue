from django.db import models

# Create your models here.
class Kommentar(models.Model):
    ueberschrift = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    kommentar = models.TextField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)