# Generated by Django 5.0.6 on 2024-06-28 18:46

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
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('248e85d7-9d33-4ba9-8b4d-5a64472fae04'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('248e85d7-9d33-4ba9-8b4d-5a64472fae04'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='foods/')),
                ('is_available', models.BooleanField(default=True)),
                ('is_popular', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discounted_price_field', models.FloatField(blank=True, null=True)),
                ('discount_percentage_field', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='foods.category')),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'foods',
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('248e85d7-9d33-4ba9-8b4d-5a64472fae04'), editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price_field', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'food order',
                'verbose_name_plural': 'food orders',
                'db_table': 'food_order',
            },
        ),
        migrations.CreateModel(
            name='FoodReview',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('248e85d7-9d33-4ba9-8b4d-5a64472fae04'), editable=False, primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'food review',
                'verbose_name_plural': 'food reviews',
                'db_table': 'food_review',
            },
        ),
    ]
