# Generated by Django 4.2.1 on 2023-05-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0002_alter_commentreport_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commentreport",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="commonreport",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="nemoreport",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="question",
            name="is_deleted",
        ),
        migrations.AddField(
            model_name="commentreport",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="commonreport",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="nemoreport",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
