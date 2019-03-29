# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class genere(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    tittle=models.CharField(max_length=255)
    release_year=models.IntegerField()
    number_in_stock=models.IntegerField()
    daily_rate=models.FloatField()
    genere=models.ForeignKey(genere,on_delete=models.CASCADE)
    data_created=models.DateTimeField(default=timezone.now)
    objects = models.Manager()