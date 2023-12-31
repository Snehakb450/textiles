# Generated by Django 4.2.4 on 2023-09-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sellers",
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
                (
                    "resel_company_name",
                    models.TextField(db_column="resel_company", max_length=50),
                ),
                (
                    "resel_company_id",
                    models.TextField(db_column="resel_id", max_length=20),
                ),
                (
                    "resel_address",
                    models.TextField(db_column="resel_address", max_length=200),
                ),
                (
                    "resel_country",
                    models.TextField(db_column="resel_country", max_length=20),
                ),
                (
                    "resel_mobile",
                    models.TextField(db_column="resel_mobile", max_length=10),
                ),
                (
                    "resel_email",
                    models.TextField(db_column="resel_email", max_length=30),
                ),
                (
                    "resel_accountholder_name",
                    models.TextField(db_column="resel_holder_name", max_length=50),
                ),
                (
                    "resel_account_number",
                    models.TextField(db_column="resel_accountnumber", max_length=50),
                ),
                (
                    "resel_ifsc_number",
                    models.TextField(db_column="resel_ifsc", max_length=30),
                ),
                ("pwd", models.TextField(db_column="pwd", max_length=10, null=True)),
                (
                    "rstatus",
                    models.TextField(
                        db_column="status", default="", max_length=50, null=True
                    ),
                ),
            ],
            options={
                "db_table": "sellers",
            },
        ),
    ]
