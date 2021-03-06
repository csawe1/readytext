# Generated by Django 3.2.3 on 2022-02-15 14:29

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wait', models.IntegerField()),
                ('party_name', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('note', models.CharField(max_length=20)),
            ],
        ),
    ]
