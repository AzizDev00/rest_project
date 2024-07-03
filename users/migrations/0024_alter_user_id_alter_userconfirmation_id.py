# Generated by Django 5.0 on 2024-07-03 06:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_user_id_alter_userconfirmation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('32d58db0-54ea-4d94-b8e7-1d99f139eeec'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('32d58db0-54ea-4d94-b8e7-1d99f139eeec'), editable=False, primary_key=True, serialize=False),
        ),
    ]
