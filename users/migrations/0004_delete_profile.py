# Generated by Django 4.2.4 on 2023-09-06 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_session_guestuser_session'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]