# Generated by Django 4.2.5 on 2023-09-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Timetable",
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
                ("title", models.CharField(max_length=50, verbose_name="title")),
            ],
            options={
                "verbose_name": "Timetable",
                "verbose_name_plural": "Timetables",
            },
        ),
    ]
