# Generated by Django 3.0.5 on 2020-04-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='Profile'),
        ),
    ]
