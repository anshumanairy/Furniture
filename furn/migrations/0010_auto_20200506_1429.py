# Generated by Django 3.0.5 on 2020-05-06 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('furn', '0009_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]