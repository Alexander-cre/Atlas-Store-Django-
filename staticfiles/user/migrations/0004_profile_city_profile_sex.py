# Generated by Django 5.1.2 on 2024-10-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_user_remove_profile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.TextField(blank=True, null=True),
        ),
    ]
