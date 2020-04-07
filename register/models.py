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

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
INTERN_CHOICES = (
    ('1','1'),
    ('2', '2-4'),
    ('3','5-10'),
    ('4','10+'),
)

TIME_CHOICES = (
    ('1','Summer Vacations (May - July)'),
    ('2', 'Winter Vacations (December - Mid-January'),
    ('3','Other (Only Work From Home Interns available)'),
)


HIRING_CHOICES = (
    ('1','Yes'),
    ('2', 'No'),
    ('3','Maybe'),
)
class UserInfo(models.Model):
    firstname = models.CharField(max_length=255, null = True)
    lastname = models.CharField(max_length=255, null = True)
    college = models.CharField(max_length=1024, verbose_name="Name of the College", null = True)
    mobile = models.CharField(max_length=10, verbose_name="Mobile Number", null = True)
    achievemennts = models.TextField(max_length=1024, verbose_name="Personal Achievements", null =True)
    profile = models.TextField(max_length=1024, verbose_name="Preferred Job Profile", null =True)
    cgpa = models.FloatField(verbose_name="CGPA (0.00 - 10.00)",
                             validators=[MaxValueValidator(10), MinValueValidator(0)], default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo", null = True)
    branch = models.CharField(max_length=255, null = True)
    email = models.EmailField(null=True)

