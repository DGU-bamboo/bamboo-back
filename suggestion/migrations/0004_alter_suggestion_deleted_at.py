# Generated by Django 4.2.1 on 2023-05-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suggestion", "0003_remove_suggestion_is_deleted_suggestion_deleted_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suggestion",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
