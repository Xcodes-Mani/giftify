# Generated by Django 4.2.4 on 2023-09-06 05:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name (optional)')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region='IN', unique=True)),
            ],
        ),
    ]