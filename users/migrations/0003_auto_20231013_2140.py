# Generated by Django 3.2.13 on 2023-10-13 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_group_groupyear'),
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
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]