# Generated by Django 3.2.13 on 2023-10-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_work_returnnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='returnNumber',
            field=models.IntegerField(default=0),
        ),
    ]
