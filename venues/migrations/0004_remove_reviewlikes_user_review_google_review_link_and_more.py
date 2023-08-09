# Generated by Django 4.1.7 on 2023-06-06 07:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venues', '0003_alter_venue_price_per_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewlikes',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='google_review_link',
            field=models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='review',
            name='google_user_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='google_user_rated',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='google_user_thumbnail',
            field=models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='review',
            name='google_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL),
        ),
    ]