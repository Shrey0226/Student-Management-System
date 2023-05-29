# Generated by Django 4.1.7 on 2023-04-12 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_remove_faculty_leave_f_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.faculty')),
            ],
        ),
    ]
