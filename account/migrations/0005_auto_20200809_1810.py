# Generated by Django 3.0.2 on 2020-08-09 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200809_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='current_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='current_city', to='account.City'),
        ),
        migrations.AddField(
            model_name='talent',
            name='home_town',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='home_town', to='account.City'),
        ),
        migrations.AddField(
            model_name='talent',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='1', max_length=30),
        ),
    ]
