# Generated by Django 3.0.5 on 2020-05-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0006_auto_20200504_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(),
        ),
    ]