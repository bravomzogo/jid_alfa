# Generated by Django 5.1.5 on 2025-01-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='title',
            new_name='Shekh',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='content',
        ),
        migrations.AddField(
            model_name='lesson',
            name='Darasa',
            field=models.TextField(default=''),
        ),
    ]
