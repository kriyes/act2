# Generated by Django 3.0.2 on 2020-08-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20200812_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='portfolio_img5',
            field=models.ImageField(blank=True, upload_to='account/'),
        ),
        migrations.AddField(
            model_name='talent',
            name='portfolio_img6',
            field=models.ImageField(blank=True, upload_to='account/'),
        ),
        migrations.AddField(
            model_name='talent',
            name='portfolio_img7',
            field=models.ImageField(blank=True, upload_to='account/'),
        ),
        migrations.AddField(
            model_name='talent',
            name='portfolio_img8',
            field=models.ImageField(blank=True, upload_to='account/'),
        ),
    ]