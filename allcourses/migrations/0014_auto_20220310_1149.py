# Generated by Django 3.1.2 on 2022-03-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcourses', '0013_course_details_video_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='video_height',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
