# Generated by Django 5.0.2 on 2024-02-29 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='lasttname',
            new_name='lastname',
        ),
    ]
