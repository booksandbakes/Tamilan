# Generated by Django 3.0.6 on 2020-07-06 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publish',
            name='Userid',
        ),
    ]