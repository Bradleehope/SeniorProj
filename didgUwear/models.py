from django.db import models


class Shirt(models.Model):
    nickname = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    secondary_color = models.CharField(max_length=30, null=True)
    occasion = models.CharField(max_length=30)
    weather = models.CharField(max_length=30, null=True)
    fit = models.CharField(max_length=30, null=True)
    holiday = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    brand = models.CharField(max_length=30)
    date = models.DateField()
    img_link = models.CharField(max_length=50)


class Pant(models.Model):
    nickname = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    secondary_color = models.CharField(max_length=30, null=True)
    occasion = models.CharField(max_length=30)
    weather = models.CharField(max_length=30, null=True)
    fit = models.CharField(max_length=30, null=True)
    holiday = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    brand = models.CharField(max_length=30)
    date = models.DateField()
    img_link = models.CharField(max_length=50)
