# Generated by Django 3.0.5 on 2024-10-25 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_librarian'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
