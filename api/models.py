# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Members(models.Model):
    keynum = models.IntegerField()
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    office = models.CharField(max_length=200)
    tac = models.CharField(max_length=200)
    hm = models.CharField(max_length=200)

    def __str__(self):
        return self.name
