from django.db import models

# Create your models here.
class User (models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    username=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.IntegerField()
    repassword=models.IntegerField()
