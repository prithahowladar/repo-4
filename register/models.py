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
    email = models.EmailField(null=True)
    company = models.CharField(max_length = 1024, verbose_name = "Name of the Company")
    intern = models.CharField(max_length=6, choices=INTERN_CHOICES, default='1', verbose_name = "Number of Interns")
    job = models.TextField(max_length=1024, verbose_name="Job Description")
    timeperiod = models.CharField(max_length=100, choices=TIME_CHOICES, default='1', verbose_name="Time period when you want the intern")
    stipend = models.CharField(max_length=1024, verbose_name="Tentative stipend (per month)")
    hiring = models.CharField(max_length=10, choices=HIRING_CHOICES, default='1', verbose_name="Are you interested in hiring permanent employees also?")
    requirements = models.TextField(max_length=1024, verbose_name="Specific requirements (Like college or stream of candidates)")

