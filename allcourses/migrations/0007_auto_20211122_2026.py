# Generated by Django 3.1.2 on 2021-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcourses', '0006_auto_20211114_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
