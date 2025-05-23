# Generated by Django 5.2.1 on 2025-05-14 14:22

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedUsers',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_users', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='assigned_userss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Assigned User',
                'verbose_name_plural': 'Assigned Users',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('completion_report', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
                ('worked_hours', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['-created_at'],
            },
        ),
    ]
