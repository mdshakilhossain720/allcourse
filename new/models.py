from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    roll=models.IntegerField()
    course=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    