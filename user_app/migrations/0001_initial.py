# Generated by Django 5.0.4 on 2024-04-16 22:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('account_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_app.appuser')),
            ],
        ),
    ]
