# Generated by Django 5.1.5 on 2025-01-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durus', '0011_alter_newz_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newz',
            name='Time',
            field=models.CharField(default='', max_length=20),
        ),
    ]
