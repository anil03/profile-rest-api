# Generated by Django 2.2.4 on 2019-08-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
