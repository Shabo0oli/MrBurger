# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels

# Create your models here.

class Answer(models.Model):
    objects = jmodels.jManager()
    Date = jmodels.jDateField(null=True)
    Time = models.TimeField(null=True)
    Sex = models.CharField(max_length=20, default='M')
    Age = models.CharField(max_length=20, default='None')
    QoProduct = models.IntegerField(default=0)
    QoDesign = models.IntegerField(default=0)
    QoResponse = models.IntegerField(default=0)
    QoDelivery = models.IntegerField(default=0)
    QoPersonality = models.IntegerField(default=0)
    QoDecor = models.IntegerField(default=0)
    QoAmount = models.IntegerField(default=0)
    QoShape = models.IntegerField(default=0)
    Comment = models.TextField(max_length=300 , blank=True)

    def __str__(self):
        return "{}  {}".format(self.Sex, self.Age)

