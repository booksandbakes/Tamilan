# Generated by Django 3.0.6 on 2020-07-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0006_auto_20200708_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='contend',
            field=models.TextField(max_length=2000),
        ),
    ]
