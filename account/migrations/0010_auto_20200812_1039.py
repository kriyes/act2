# Generated by Django 3.0.2 on 2020-08-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200811_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
    ]
