# Generated by Django 3.1.2 on 2021-11-08 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0027_auto_20211108_1848'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allcourses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
                ('enrolled_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
