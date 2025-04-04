# Generated by Django 5.1.4 on 2025-03-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_companyprofile_level_alter_level1profile_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level3profile',
            old_name='intro_video',
            new_name='intro_video_link',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='profile_picture_company',
            field=models.ImageField(blank=True, null=True, upload_to='companies/'),
        ),
    ]
