# Generated by Django 4.1.7 on 2023-04-07 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_faculty_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty_notification',
            old_name='staff_id',
            new_name='faculty_id',
        ),
    ]
