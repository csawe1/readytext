# Generated by Django 3.2.12 on 2022-03-17 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_waitlist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='delay',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_context',
        ),
    ]
