# Generated by Django 4.0.6 on 2024-02-21 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_project_button_description_project_button_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='show_or_hide',
            new_name='show',
        ),
    ]
