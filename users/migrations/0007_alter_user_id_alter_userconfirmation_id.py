# Generated by Django 5.0.6 on 2024-06-28 18:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_id_alter_userconfirmation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('76422471-9d80-4ec6-9c82-3598516ed020'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('76422471-9d80-4ec6-9c82-3598516ed020'), editable=False, primary_key=True, serialize=False),
        ),
    ]