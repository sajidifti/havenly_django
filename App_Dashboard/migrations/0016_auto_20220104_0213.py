# Generated by Django 2.1.11 on 2022-01-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0015_auto_20220104_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='post',
            field=models.IntegerField(),
        ),
    ]
