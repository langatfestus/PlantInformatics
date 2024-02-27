from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    planting_season = models.CharField(max_length=50)
    harvest_season = models.CharField(max_length=50)
    maturity_period = models.CharField(max_length=50)
    image = models.ImageField(upload_to='crops/images', blank=True, null=True)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
