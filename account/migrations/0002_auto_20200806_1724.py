# Generated by Django 3.0.2 on 2020-08-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='agency_signed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talent',
            name='exprienced',
            field=models.BooleanField(default=False),
        ),
    ]
