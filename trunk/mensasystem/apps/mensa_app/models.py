#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django_countries.fields import CountryField



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    skype = models.CharField(max_length=255)
    department = models.CharField(max_length=1000)
    position = models.CharField(max_length=255)

    def __unicode__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    actualStartTime = models.TimeField()
    actualEndTime = models.TimeField()
    planStartTime = models.DateTimeField()
    planEndTime = models.DateTimeField()
    status = models.CharField(max_length=50)

class ProjectUser(models.Model):
    user = models.ForeignKey(User)
    project = models.ManyToManyField(Project)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    project = models.ForeignKey(Project)
    actualStartTime = models.TimeField()
    actualEndTime = models.TimeField()
    planStartTime = models.DateTimeField()
    planEndTime = models.DateTimeField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User)


class Setting(models.Model):
    key = models.CharField(max_length=10)
    value = models.CharField(max_length=50)

