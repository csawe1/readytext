# Generated by Django 3.2.12 on 2022-02-22 05:04

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_waitlist_time_message_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('party_name', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('state', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
            ],
        ),
    ]
