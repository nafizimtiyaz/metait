# Generated by Django 3.1.2 on 2022-04-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0036_course_intro_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='intro_video',
            field=models.FileField(blank=True, default=True, upload_to='video'),
            preserve_default=False,
        ),
    ]