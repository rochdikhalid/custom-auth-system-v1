# Generated by Django 3.2.7 on 2021-10-11 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customuser_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='updated_at',
        ),
    ]
