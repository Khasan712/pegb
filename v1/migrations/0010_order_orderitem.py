# Generated by Django 5.0 on 2023-12-14 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0009_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('new', 'new'), ('proccess', 'proccess'), ('done', 'done'), ('rejected', 'rejected')], default='new', max_length=8)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]