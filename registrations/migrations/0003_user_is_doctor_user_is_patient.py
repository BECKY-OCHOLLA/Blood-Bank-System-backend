# Generated by Django 4.0.5 on 2022-07-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_doctor_user_is_donor_delete_admin_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]