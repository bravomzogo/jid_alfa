# Generated by Django 5.1.5 on 2025-01-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durus', '0013_qur'),
    ]

    operations = [
        migrations.AddField(
            model_name='qur',
            name='sura',
            field=models.CharField(default='', max_length=200),
        ),
    ]
