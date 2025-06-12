from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):

    STATUS_CHOICES = [
        ('done','Done'),
        ('pending', 'Pending'),
    ]


    title = models.CharField(max_length=200)
    deadline = models.DateField()
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES , default='pending')
    task_user = models.ForeignKey(User , on_delete=models.CASCADE)


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=150)
#     price = models.FloatField()
#     number = models.IntegerField()

# class Rating()