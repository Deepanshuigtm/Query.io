# Generated by Django 4.0.5 on 2023-10-11 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squery', '0004_querypost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='querypost',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='votes_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]