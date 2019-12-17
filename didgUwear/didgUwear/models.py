from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

clothing_url = FileSystemStorage(location=settings.CLOTHING_URL)


class Shirt(models.Model):
    nickname = models.CharField(max_length=50, null=True, unique=True)
    primary_color = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    secondary_color = models.CharField(max_length=30, null=True)
    occasion = models.CharField(max_length=30)
    weather = models.CharField(max_length=30, null=True)
    pattern = models.CharField(max_length=30, null=True)
    holiday = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=30)
    date_added = models.DateField()
    img_link = models.FileField(storage=clothing_url)


class Pant(models.Model):
    nickname = models.CharField(max_length=50, null=True)
    primary_color = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=30)
    date_added = models.DateField()
    img_link = models.FileField(storage=clothing_url)