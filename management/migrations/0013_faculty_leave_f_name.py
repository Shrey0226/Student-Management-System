# Generated by Django 4.1.7 on 2023-04-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_faculty_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_leave',
            name='f_name',
            field=models.TextField(default='None'),
        ),
    ]
