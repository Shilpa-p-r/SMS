# Generated by Django 3.0.5 on 2024-10-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0020_remove_library_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='library_history', to='school.StudentExtra'),
        ),
        migrations.AlterField(
            model_name='library',
            name='book_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]