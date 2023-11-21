# Generated by Django 3.2.13 on 2023-10-13 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_task_worknumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='workNumber',
            field=models.PositiveIntegerField(default=111, validators=[django.core.validators.MinValueValidator(111), django.core.validators.MaxValueValidator(999)]),
        ),
    ]
