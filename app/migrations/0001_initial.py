# Generated by Django 4.1.1 on 2022-09-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("url", models.URLField(unique=True)),
                ("url_hash", models.CharField(blank=True, max_length=256)),
                ("short_url", models.URLField(blank=True, unique=True)),
                ("clicks", models.IntegerField(default=0)),
                ("time_click", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
    ]
