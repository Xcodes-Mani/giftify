# Generated by Django 4.2.4 on 2023-09-06 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Mani', max_length=255)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(default='+91908750532', max_length=13, region='IN', unique=True)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('city_district_town', models.CharField(max_length=255, verbose_name='City/District/Town')),
                ('state', models.CharField(choices=[('Andaman and Nicobar islands', 'Andaman and Nicobar islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunacal Pradesh', 'Arunacal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli & Daman & Diu', 'Dadra & Nagar Haveli & Daman & Diu'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkand', 'Jharkand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telanga', 'Telanga'), ('Tripura', 'Tripura'), ('Uttarkhand', 'Uttarkhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=40)),
                ('landmark', models.CharField(blank=True, max_length=255, null=True, verbose_name='Landmark (optional)')),
                ('alternate_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=13, null=True, region='IN', verbose_name='Alternate Mobile Number (optional)')),
            ],
            options={
                'verbose_name': 'User address',
                'verbose_name_plural': 'User addresses',
            },
        ),
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
        migrations.AddField(
            model_name='address',
            name='guest_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guest_address', to='users.guestuser'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
