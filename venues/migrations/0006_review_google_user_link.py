# Generated by Django 4.1.7 on 2023-06-06 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0005_review_google_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='google_user_link',
            field=models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
    ]
