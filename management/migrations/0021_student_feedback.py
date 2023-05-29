# Generated by Django 4.1.7 on 2023-04-23 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_student_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
    ]
