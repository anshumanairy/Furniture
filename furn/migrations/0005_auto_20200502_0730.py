# Generated by Django 3.0.5 on 2020-05-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0004_auto_20200502_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_upload',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
