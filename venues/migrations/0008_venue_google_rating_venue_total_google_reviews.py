# Generated by Django 4.1.7 on 2023-06-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_alter_review_google_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='google_rating',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='total_google_reviews',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
