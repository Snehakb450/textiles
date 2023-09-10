# Generated by Django 4.2.4 on 2023-09-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("username", models.CharField(db_column="username", max_length=20)),
                ("password", models.CharField(db_column="password", max_length=20)),
            ],
            options={
                "db_table": "data",
            },
        ),
    ]