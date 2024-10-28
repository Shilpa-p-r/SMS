# Generated by Django 3.0.5 on 2024-10-26 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0021_auto_20241026_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='student',
        ),
        migrations.RenameField(
            model_name='studentextra',
            old_name='roll',
            new_name='roll_no',
        ),
        migrations.RemoveField(
            model_name='studentextra',
            name='fee',
        ),
        migrations.AddField(
            model_name='studentextra',
            name='book_borrow_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='book_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='bookdue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='pay_duedate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='payment_method',
            field=models.CharField(choices=[('card', 'CARD'), ('cash', 'CASH'), ('upi_transfer', 'UPI TRANSFER')], default='cash', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='student_fees',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Fees',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]