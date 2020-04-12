from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    company= models.CharField(max_length = 255, null =True)
    profile = models.CharField(max_length=255, null=True)
    vacancy = models.CharField(max_length = 255, null =True)
    location= models.CharField(max_length=255, null=True)
class CheckBox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="job", null=True)
    choice1 = models.BooleanField(default= False)
    choice2 = models.BooleanField(default= False)
    choice3 = models.BooleanField(default=False)