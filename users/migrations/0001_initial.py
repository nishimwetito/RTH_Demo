# Generated by Django 5.2 on 2025-04-04 11:22

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW')),
                ('profile_picture_company', models.ImageField(blank=True, null=True, upload_to='companies/')),
                ('profile_picture_logo', models.ImageField(blank=True, null=True, upload_to='companies/')),
                ('services', models.TextField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('level', models.CharField(choices=[('level1', 'Level 1 - Skilled but No Certification'), ('level2', 'Level 2 - Certified Professional'), ('level3', 'Level 3 - Expert/Business'), ('company', 'Company Hiring')], default='company', editable=False, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW')),
                ('profile_picture', models.ImageField(upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to='users.profile')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='users.category')),
            ],
        ),
        migrations.CreateModel(
            name='Level3Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('education', models.TextField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('intro_video_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('level', models.CharField(choices=[('level1', 'Level 1 - Skilled but No Certification'), ('level2', 'Level 2 - Certified Professional'), ('level3', 'Level 3 - Expert/Business'), ('company', 'Company Hiring')], default='level3', editable=False, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, related_name='level3_profiles', to='users.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Level2Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('level', models.CharField(choices=[('level1', 'Level 1 - Skilled but No Certification'), ('level2', 'Level 2 - Certified Professional'), ('level3', 'Level 3 - Expert/Business'), ('company', 'Company Hiring')], default='level2', editable=False, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, related_name='level2_profiles', to='users.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Level1Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('level', models.CharField(choices=[('level1', 'Level 1 - Skilled but No Certification'), ('level2', 'Level 2 - Certified Professional'), ('level3', 'Level 3 - Expert/Business'), ('company', 'Company Hiring')], default='level1', editable=False, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_profiles', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, related_name='level1_profiles', to='users.skill')),
            ],
        ),
    ]
