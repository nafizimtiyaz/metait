# Generated by Django 3.1.2 on 2021-11-08 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0027_auto_20211108_1848'),
        ('allcourses', '0003_auto_20211108_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enrolled_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course'),
        ),
    ]
