# Generated by Django 3.2.13 on 2023-10-13 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20231013_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='groupNumber',
        ),
        migrations.RemoveField(
            model_name='group',
            name='groupYear',
        ),
    ]
