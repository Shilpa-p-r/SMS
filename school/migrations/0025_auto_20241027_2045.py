# Generated by Django 3.0.5 on 2024-10-27 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0024_studentextra_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentExtra',
            new_name='Students',
        ),
    ]
