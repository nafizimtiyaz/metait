# Generated by Django 3.2.6 on 2021-09-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210916_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]