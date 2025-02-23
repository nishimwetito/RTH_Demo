from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Level1Profile,Level2Profile,Level3Profile,CompanyProfile

# Base user registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','phone','address','profile_picture']


class Level1ProfileForm(forms.ModelForm):
    class Meta:
        model = Level1Profile
        exclude = ['user','created_at','level']

class Level2ProfileForm(forms.ModelForm):
    class Meta:
        model = Level2Profile
        exclude = ['user','created_at','level']

class Level3ProfileForm(forms.ModelForm):
    class Meta:
        model = Level3Profile
        exclude = ['user','created_at','level']
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ['user','created_at','level']


   





    






