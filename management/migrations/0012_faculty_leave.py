# Generated by Django 4.1.7 on 2023-04-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_faculty_notification_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.faculty')),
            ],
        ),
    ]
