# Generated by Django 3.0.2 on 2020-08-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200812_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='about_myself',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]