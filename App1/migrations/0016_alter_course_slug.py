# Generated by Django 3.2.6 on 2021-09-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0015_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]