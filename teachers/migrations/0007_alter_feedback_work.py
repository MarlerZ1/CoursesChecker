# Generated by Django 3.2.13 on 2023-10-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20231015_2042'),
        ('teachers', '0006_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.work'),
        ),
    ]
