# Generated by Django 3.2.8 on 2023-06-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='name',
            new_name='university_name',
        ),
    ]
