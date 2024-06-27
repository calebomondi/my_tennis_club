from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=255,null=True)
    