# Generated by Django 5.2.1 on 2025-05-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.CharField(),
        ),
    ]
