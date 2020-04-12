
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length = 255, null =True)
    email = models.EmailField(null = True)
    mobile = models.CharField(max_length = 10, verbose_name = "Mobile Number", null = True)
    address = models.TextField(max_length = 1024, verbose_name = "Address", null = True)
    city =  models.CharField(max_length = 50, null = True)

    #
    #college = models.CharField(max_length = 1024, verbose_name = "Name of the College",null = True)
    ##university = models.CharField(max_length = 1024, verbose_name = "Name of the University",null = True)
    #unicityandstate= models.CharField(max_length = 1024, verbose_name = "Uni City and State",null = True)
    #degree = models.BooleanField(null = True)
    #field = models.CharField(max_length = 1024, verbose_name = "Field of study",null = True)
    #graduationyear = models.FloatField(verbose_name = "Graduation year", validators = [MaxValueValidator(2000), MinValueValidator(2025)], default = 2020)
    #highschool = models.CharField(max_length = 1024, verbose_name = "Name of the High School",null = True)
    #hspercentage = models.CharField(max_length = 10, verbose_name = "high school percentage",null = True)
    #hsyear = models.FloatField(verbose_name = "High School Graduation year", validators = [MaxValueValidator(2000), MinValueValidator(2025)], default = 2020)
    #hscityandstate= models.CharField(max_length = 1024, verbose_name = "HS City and State",null = True)
    #ssschool = models.CharField(max_length = 1024, verbose_name = "Name of the SS School",null = True)
    #sspercentage = models.CharField(max_length = 10, verbose_name = "ss school percentage",null = True)
    #ssyear = models.FloatField(verbose_name = "ss School Graduation year", validators = [MaxValueValidator(2000), MinValueValidator(2025)], default = 2020)
    #sscityandstate= models.CharField(max_length = 1024, verbose_name = "ss City and State",null = True)

   # achievements = models.TextField(max_length = 1024, verbose_name = "Personal Achievements")
   # profile = models.TextField(max_length = 1024, verbose_name = "Preferred Job Profile")
   # cgpa = models.FloatField(verbose_name = "CGPA (0.00 - 10.00)", validators = [MaxValueValidator(10), MinValueValidator(0)], default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "userinfo", null = True)
    #branch = models.CharField(max_length = 255)
