from django.db import models


class Rabbit(models.Model):
    # ID = models.AutoField()
    Nickname = models.CharField(max_length=200)
    Age = models.PositiveSmallIntegerField(default=0)
    Breed = models.CharField(max_length=500)
    Color = models.CharField(max_length=100)
