# Generated by Django 3.2.11 on 2022-01-28 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='users-image/'),
            preserve_default=False,
        ),
    ]
