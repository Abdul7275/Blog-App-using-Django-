from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here and are used to create database tables.
class info(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.fname


class blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now=True)
    image=models.FileField(default='none')
    def __unicode__(self):
        return self.title


    





     
'''
class upload_image(models.Model):
    img_name=models.CharField(max_length=50)
    image=models.FileField()

    def __unicode__(self):
        return self.img_name
'''
