# Generated by Django 4.0.5 on 2023-09-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Roll_number', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
                ('Email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
