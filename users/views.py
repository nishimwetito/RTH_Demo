from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm
from. forms import ProfileForm,Level1ProfileForm,Level2ProfileForm,Level3ProfileForm,CompanyProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'You are logged in as {username}.')
                return redirect('index')
            else:
                messages.error(request,'Something went wrong!')

        else:
            messages.error(request,f'An error occured!')
    else:
        login_form = AuthenticationForm()

    return render(request,'users/login.html',{'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect('register')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user) 
             # Get the profile type from the form submission
            profile_type = request.POST.get('profile_type')

            # Redirect based on the chosen profile type
            if profile_type == 'level1':
                return redirect('level1_dashboard')  # Update with actual URL name
            elif profile_type == 'level2':
                return redirect('level2_dashboard')
            elif profile_type == 'level3':
                return redirect('level3_dashboard')
            elif profile_type == 'company':
                return redirect('company_dashboard')
            else:
                return redirect('index')  # Default fallback  

                
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {
        'form': form,
    })



def level1_dashboard(request):
    if request.method == 'POST':
        form = Level1ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            level1_profile = form.save(commit=False)
            level1_profile.user = request.user
            level1_profile.save()
            return redirect('index')
    else:
        form = Level1ProfileForm()

      

    return render(request, 'users/level1.html',{'form':form})

def level2_dashboard(request):
    if request.method == 'POST':
        form = Level2ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            level2_profile = form.save(commit=False)
            level2_profile.user= request.user
            level2_profile.save()
            return redirect('index')
    else:
        form = Level2ProfileForm()  

    return render(request, 'users/level2.html', {'form': form})


def level3_dashboard(request):
    if request.method == 'POST':
        form = Level3ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            level3_profile = form.save(commit=False)
            level3_profile.user = request.user
            level3_profile.save()
            return redirect('index')

    else:
         form = Level1ProfileForm()
  
   
    return render(request, 'users/level3.html',{'form':form})

def company_dashboard(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST,request.FILES)
        if form.is_valid():
            company_profile = form.save(commit=False)
            company_profile.user = request.user
            company_profile.save()
            return redirect('index')
    else:

        form =  CompanyProfileForm()
    
    
    return render(request, 'users/company.html',{'form':form})

