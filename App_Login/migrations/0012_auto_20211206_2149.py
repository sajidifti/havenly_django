# Generated by Django 2.1.11 on 2021-12-06 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0011_auto_20211206_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_country', to='App_Dashboard.Country'),
        ),
    ]
