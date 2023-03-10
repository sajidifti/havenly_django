# Generated by Django 2.1.11 on 2021-12-06 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0008_post'),
        ('App_Login', '0006_auto_20211203_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_country_info', to='App_Dashboard.Country'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Deactivate')], null=True),
        ),
    ]
