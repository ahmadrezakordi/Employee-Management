# Generated by Django 5.0.7 on 2024-08-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birthday_email_sent',
            field=models.BooleanField(default=False),
        ),
    ]