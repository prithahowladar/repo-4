# Generated by Django 2.0.13 on 2020-04-11 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='choice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to=settings.AUTH_USER_MODEL),
        ),
    ]