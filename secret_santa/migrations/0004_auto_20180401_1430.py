# Generated by Django 2.0.1 on 2018-04-01 18:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('secret_santa', '0003_listgiftpairing'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftListPairing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('gift_pair_members', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)])),
                ('gift_pair_original_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secret_santa.List')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='listgiftpairing',
            name='gift_pair_member',
        ),
        migrations.RemoveField(
            model_name='listgiftpairing',
            name='gift_pair_original_list',
        ),
        migrations.DeleteModel(
            name='ListGiftPairing',
        ),
    ]
