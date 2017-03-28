from __future__ import unicode_literals
from .. login.models import User #im port the user
from django.db import models

class MainManager(models.Manager):
    def first_method(self, postData):
        return
    def other_method(self, postData):
        return

# Create your models here.
class Main(models.Model):
    #put in links to user and to other models
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MainManager()
