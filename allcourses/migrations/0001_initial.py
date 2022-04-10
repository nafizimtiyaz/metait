# Generated by Django 3.1.2 on 2021-11-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App1', '0027_auto_20211108_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(max_length=100, null=True)),
                ('lecture_body', models.TextField(max_length=10000, null=True)),
                ('lecture_imgae', models.ImageField(upload_to='all_courses')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
            ],
        ),
    ]