# Generated by Django 3.2.6 on 2021-09-16 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210916_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='phone',
        ),
    ]