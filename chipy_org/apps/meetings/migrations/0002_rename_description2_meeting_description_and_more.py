# Generated by Django 5.1.3 on 2024-11-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0001_squash_to_0013"),
    ]

    operations = [
        migrations.RenameField(
            model_name="meeting",
            old_name="description2",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="meetingtype",
            old_name="description2",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="topic",
            old_name="description2",
            new_name="description",
        ),
    ]