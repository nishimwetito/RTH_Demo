from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# User Profile Model with different levels
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=False, region="RW")  # Default country: Rwanda
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



# Address Model
class Address(models.Model):
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.village}, {self.cell}, {self.sector}, {self.district}, {self.province}"

# Category Model (e.g., Construction, Event Services, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Skill Model (e.g., Plumbing, Carpentry, etc.)
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name




# Profiles
class Level1Profile(models.Model):
    LEVEL_CHOICES = [
        ('level1', 'Level 1 - Skilled but No Certification'),
        ('level2', 'Level 2 - Certified Professional'),
        ('level3', 'Level 3 - Expert/Business'),
        ('company', 'Company Hiring'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique=False, region="RW")  # Default country: Rwanda
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='level1_profiles', blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES,default='level1',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set level for new instances
            self.level = 'level1'
        super().save(*args, **kwargs)  # Call Django’s original save method

class Level2Profile(models.Model):
    LEVEL_CHOICES = [
        ('level1', 'Level 1 - Skilled but No Certification'),
        ('level2', 'Level 2 - Certified Professional'),
        ('level3', 'Level 3 - Expert/Business'),
        ('company', 'Company Hiring'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique=False, region="RW")  # Default country: Rwanda
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='level2_profiles', blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES,default='level2',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set level for new instances
            self.level = 'level1'
        super().save(*args, **kwargs)  # Call Django’s original save method

class Level3Profile(models.Model):
    LEVEL_CHOICES = [
        ('level1', 'Level 1 - Skilled but No Certification'),
        ('level2', 'Level 2 - Certified Professional'),
        ('level3', 'Level 3 - Expert/Business'),
        ('company', 'Company Hiring'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique=False, region="RW")  # Default country: Rwanda
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    intro_video = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)

    skills = models.ManyToManyField(Skill, related_name='level3_profiles', blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES,default='level3',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set level for new instances
            self.level = 'level1'
        super().save(*args, **kwargs)  # Call Django’s original save method

class CompanyProfile(models.Model):
    LEVEL_CHOICES = [
        ('level1', 'Level 1 - Skilled but No Certification'),
        ('level2', 'Level 2 - Certified Professional'),
        ('level3', 'Level 3 - Expert/Business'),
        ('company', 'Company Hiring'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique=False, region="RW")  # Default country: Rwanda
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture_logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES,default='company',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
   

