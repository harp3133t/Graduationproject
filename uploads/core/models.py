#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Document(models.Model):
    author = models.CharField(max_length=255, blank=True)#.ForeignKey('auth.User')
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.uploaded_at=timezone.now()
        self.save()

    def  __unicode__(self):
        return self.description

class CustomerData(models.Model):
    number = models.IntegerField()
    count = models.IntegerField()
    name = models.CharField(max_length=30,blank=True)
    def publish(self):
        self.uploaded_at=timezone.now()
        self.save()
    def  __unicode__(self):
        return self.name