# Generated by Django 5.1.6 on 2025-02-07 18:37

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, unique=True)),
                ('select_days', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=56)),
                ('created_date', models.DateTimeField(blank=True, null=True, verbose_name='creation_date')),
                ('students', models.ManyToManyField(blank=True, to='users.student')),
            ],
        ),
    ]
