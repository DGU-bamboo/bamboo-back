# Generated by Django 4.2.1 on 2023-05-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0004_alter_comment_approved_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
