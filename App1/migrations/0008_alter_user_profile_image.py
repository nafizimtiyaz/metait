# Generated by Django 3.2.6 on 2021-08-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.URLField(),
        ),
    ]
