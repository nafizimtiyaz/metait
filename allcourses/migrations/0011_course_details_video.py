# Generated by Django 3.1.2 on 2022-03-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcourses', '0010_course_details_link_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_details',
            name='video',
            field=models.FileField(default=True, upload_to='video'),
            preserve_default=False,
        ),
    ]