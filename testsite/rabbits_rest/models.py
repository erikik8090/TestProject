from django.db import models


class Rabbit(models.Model):
    Nickname = models.CharField(max_length=200)
    Age = models.PositiveSmallIntegerField(default=0)
    Breed = models.CharField(max_length=500, default='Unknown')
    Color = models.CharField(max_length=100, default='Unknown')
