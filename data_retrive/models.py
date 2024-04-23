from django.db import models

# Create your models here.
class user_details(models.Model):
    name=models.CharField(max_length=300)
    mark=models.IntegerField()
    college=models.TextField()

class student(models.Model):
    diff_values=[('fullstack','FullStack'),('devops','Devops'),('ai&ml','AI&ML')]
    name=models.CharField(max_length=300)
    courses=models.CharField(max_length=200,choices=diff_values,default='fullstack')


