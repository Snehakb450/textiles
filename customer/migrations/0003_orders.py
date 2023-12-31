# Generated by Django 4.2.4 on 2023-09-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("seller", "0003_products"),
        ("customer", "0002_remove_customer_customer_country"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("quantity", models.IntegerField(db_column="quantity")),
                ("status", models.TextField(db_column="status", max_length=20)),
                (
                    "customer_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seller.products",
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
    ]
