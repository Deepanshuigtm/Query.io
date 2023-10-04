# Generated by Django 4.2.2 on 2023-10-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("squery", "0002_querypost"),
    ]

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("Roll_number", models.CharField(max_length=100)),
                ("Password", models.CharField(max_length=50)),
                ("Email_address", models.EmailField(max_length=254)),
            ],
        ),
    ]