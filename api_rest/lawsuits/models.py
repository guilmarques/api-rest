# -*- coding: utf-8 -*-
from django.db import models

class Lawsuit(models.Model):
    data = models.CharField(u'Dados do Processo', max_length=500)
    number = models.CharField(u'Número do Processo', max_length=20)
    user = models.ForeignKey('auth.User', verbose_name='Usuario', related_name='lawsuits')

    class Meta:
        ordering = ('id',)


from lawsuits.signals import *