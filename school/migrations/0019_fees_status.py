# Generated by Django 3.0.5 on 2024-10-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_auto_20241026_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]