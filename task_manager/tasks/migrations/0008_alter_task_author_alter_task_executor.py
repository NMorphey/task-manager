# Generated by Django 5.0.4 on 2024-05-22 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_author_alter_task_description_and_more'),
        ('users', '0004_delete_customuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_tasks', to='users.user', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executing_tasks', to='users.user', verbose_name='Executor'),
        ),
    ]
