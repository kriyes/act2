# Generated by Django 3.0.2 on 2020-08-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200812_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talent',
            old_name='Portfolio',
            new_name='your_best_image1',
        ),
        migrations.AddField(
            model_name='talent',
            name='your_best_image2',
            field=models.ImageField(blank=True, upload_to='account/'),
        ),
    ]
