# Generated by Django 2.1.11 on 2021-12-06 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0010_react'),
        ('App_Login', '0014_remove_userprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='country_user_profile', to='App_Dashboard.Country'),
        ),
    ]
