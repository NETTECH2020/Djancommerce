from django.db import models
from django.db.models.fields import CharField


class SA(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Email=CharField(max_length=100)
    PhoneNo=models.IntegerField()
