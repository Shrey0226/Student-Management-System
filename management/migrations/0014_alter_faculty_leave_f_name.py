# Generated by Django 4.1.7 on 2023-04-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_faculty_leave_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_leave',
            name='f_name',
            field=models.TextField(default='none'),
        ),
    ]
