# Generated by Django 3.0 on 2020-01-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='requirements',
            field=models.TextField(max_length=1024, verbose_name='Specific requirements (Like college or stream of candidates)'),
        ),
    ]
