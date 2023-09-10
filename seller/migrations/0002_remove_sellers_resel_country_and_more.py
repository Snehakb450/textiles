# Generated by Django 4.2.4 on 2023-09-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seller", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sellers",
            name="resel_country",
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_account_number",
            field=models.TextField(db_column="accountnumber", max_length=50),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_accountholder_name",
            field=models.TextField(db_column="holder_name", max_length=50),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_address",
            field=models.TextField(db_column="address", max_length=200),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_company_id",
            field=models.TextField(db_column="companyid", max_length=20),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_company_name",
            field=models.TextField(db_column="companyname", max_length=50),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_email",
            field=models.TextField(db_column="email", max_length=30),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_ifsc_number",
            field=models.TextField(db_column="ifsc", max_length=30),
        ),
        migrations.AlterField(
            model_name="sellers",
            name="resel_mobile",
            field=models.TextField(db_column="mobile", max_length=10),
        ),
    ]
