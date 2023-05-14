# Generated by Django 4.2.1 on 2023-05-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("COMMON", "COMMON"),
                            ("NEMO", "NEMO"),
                            ("ADMIN", "ADMIN"),
                        ],
                        max_length=15,
                    ),
                ),
                ("content", models.TextField()),
                ("is_student", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
