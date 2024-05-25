# Generated by Django 5.0.6 on 2024-05-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_team_members_alter_task_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dependencies',
            field=models.ManyToManyField(blank=True, null=True, related_name='dependent_tasks', to='projects.task'),
        ),
    ]