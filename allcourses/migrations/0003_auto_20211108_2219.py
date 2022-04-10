# Generated by Django 3.1.2 on 2021-11-08 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0027_auto_20211108_1848'),
        ('allcourses', '0002_enroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enrolled_course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App1.course'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='enrolled_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]