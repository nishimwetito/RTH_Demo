# Generated by Django 5.2 on 2025-04-18 08:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_message_recipient_alter_message_sender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='level2profile',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_level2_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
