# Generated by Django 5.2.1 on 2025-05-30 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
