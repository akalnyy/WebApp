"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Users(models.Model):
    title = models.CharField('usr_name', max_length=50)
    title = models.CharField('pwd', max_length=20)