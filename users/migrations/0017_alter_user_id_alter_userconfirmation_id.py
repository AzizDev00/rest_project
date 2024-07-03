# Generated by Django 5.0 on 2024-07-03 06:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_id_alter_userconfirmation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('50a761d4-6754-4cd0-9c7e-3e18ce8cc652'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('50a761d4-6754-4cd0-9c7e-3e18ce8cc652'), editable=False, primary_key=True, serialize=False),
        ),
    ]
