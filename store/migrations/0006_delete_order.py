# Generated by Django 4.2.4 on 2023-09-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]