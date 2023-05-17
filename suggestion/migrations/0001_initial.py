# Generated by Django 4.2.1 on 2023-05-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("content", models.TextField(default="")),
                ("contact", models.EmailField(blank=True, max_length=254, null=True)),
                ("memo", models.TextField(blank=True, default="")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
