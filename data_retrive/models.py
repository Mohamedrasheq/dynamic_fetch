from django.db import models

# Create your models here.
class user_details(models.Model):
    name=models.CharField(max_length=300)
    mark=models.IntegerField()
    college=models.TextField()
