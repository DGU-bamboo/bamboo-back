# Generated by Django 4.2.1 on 2023-05-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_alter_post_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="is_deleted",
        ),
        migrations.AddField(
            model_name="post",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
