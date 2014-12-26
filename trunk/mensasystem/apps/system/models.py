#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class SystemIP(models.Model):
    ip = models.IPAddressField()
    class Meta:
        verbose_name_plural = u'Thiết Lập IP'

