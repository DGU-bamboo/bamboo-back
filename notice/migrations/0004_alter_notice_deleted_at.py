# Generated by Django 4.2.1 on 2023-05-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notice", "0003_remove_notice_is_deleted_notice_deleted_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
