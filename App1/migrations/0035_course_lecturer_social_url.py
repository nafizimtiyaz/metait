# Generated by Django 3.1.2 on 2022-03-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0034_course_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lecturer_Social_url',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
