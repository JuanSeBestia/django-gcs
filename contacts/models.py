from django.db import models
from django import forms


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    photo = models.ImageField(upload_to='contacts')