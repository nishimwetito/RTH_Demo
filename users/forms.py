from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Level1Profile,Level2Profile,Level3Profile,CompanyProfile,Message

# Base user registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name'}
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # Add a base class to all fields
            field.widget.attrs.update({'class': 'input'})
            
            # Add specific classes based on the field type
            if name == 'username':
                field.widget.attrs.update({'placeholder': 'Enter your username'})
            elif name == 'email':
                field.widget.attrs.update({'placeholder': 'Enter your email'})
            elif name == 'first_name':
                field.widget.attrs.update({'placeholder': 'Enter your name'})
            elif name in ['password1', 'password2']:
                field.widget.attrs.update({'placeholder': 'Enter your password'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','phone','address','profile_picture']


class Level1ProfileForm(forms.ModelForm):
    class Meta:
        model = Level1Profile
        exclude = ['user','created_at','level','likes','address','next_available_date']

class Level2ProfileForm(forms.ModelForm):
    class Meta:
        model = Level2Profile
        exclude = ['user','created_at','level','address','next_available_date','likes']

class Level3ProfileForm(forms.ModelForm):
    class Meta:
        model = Level3Profile
        exclude = ['user','created_at','level','address','next_available_date','likes']
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ['user','created_at','level','address','likes']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


 





    






