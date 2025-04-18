from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from. forms import ProfileForm,Level1ProfileForm,Level2ProfileForm,Level3ProfileForm,CompanyProfileForm,MessageForm
from . models import Level1Profile,Level2Profile,Level3Profile, CompanyProfile,Message,Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')
#_____________________________User authentication _______________________________________

#Login a user in

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
                return redirect('home')
            else:
                messages.error(request,'Something went wrong!')

        else:
            messages.error(request,f'An error occured!')
    else:
        login_form = AuthenticationForm()

    return render(request,'users/login.html',{'login_form':login_form})

# Logout a user

def logout_view(request):
    logout(request)
    return redirect('register')

# Registering a User

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



# ____________________________________Creating profile levels__________________________________________

# Level1_Profile

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



# Level2

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

# Level3

def level3_dashboard(request):
    if request.method == 'POST':
        form = Level3ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            level3_profile = form.save(commit=False)
            level3_profile.user = request.user
            level3_profile.save()
            return redirect('index')

    else:
         form = Level3ProfileForm()
  
   
    return render(request, 'users/level3.html',{'form':form})

# Company

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


def user_profile_view(request):
    return render(request,'profile_user.html')

def company_profile_view(request):
    return render(request,'profile_company.html')

def profile2_view(request):
    return render(request,'profile_2.html')

def profile1_view(request):

    return render(request,'profile_1.html')

def profile3_view(request):
    return render(request,'profile_3.html')

def home_view(request):
    return render(request,'home.html')

def allprofiles2_view(request):
    profiles2 = Level2Profile.objects.all()
    context = {
        'profiles2':profiles2
    }
    return render(request,'allprofile2.html',context)

# Profile details

def level2_profile_detail(request, pk):
    profile = get_object_or_404(Level2Profile, pk=pk)
    return render(request, 'level2_profile_detail.html', {'profile': profile})

#Company profiles

def allcompanyprofiles_view(request):
    companies =  CompanyProfile.objects.all()
    context = {
        'companies':companies
    }
    return render(request,'allcompanyprofiles.html',context)

def allprofiles3_view(request):
    profiles3 = Level3Profile.objects.all()
    context = {
        'profiles3':profiles3
    }
    return render(request,'allprofile3.html',context)

def allprofiles1_view(request):
    profiles1 =  Level1Profile.objects.all()
    context = {
        'profiles1':profiles1
    }
    return render(request,'allprofile1.html',context)


    #_____________________Liking profile________________________________
#Profile 1
@require_POST
@login_required
def like_profile(request, profile_id):
    profile = get_object_or_404(Level1Profile, id=profile_id)
    liked = False
    
    if request.user in profile.likes.all():
        profile.likes.remove(request.user)
    else:
        profile.likes.add(request.user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'total_likes': profile.likes.count()
    })




#Like_Level_2_Profile
@require_POST
@login_required
def like_level2_profile(request, profile_id):
    profile = get_object_or_404(Level2Profile, id=profile_id)
    liked = False
    
    if request.user in profile.likes.all():
        profile.likes.remove(request.user)
    else:
        profile.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': profile.likes.count()
    })

#________________________________Sending messages________________________________

@login_required(login_url='login')
def inbox_view(request):
    profile = request.user.profile
    messagesRequests = profile.messages.all()
    unreadCount = messagesRequests.filter(is_read=False).count()
    context = {
        'messagesRequests':messagesRequests ,
        'unreadCount':unreadCount, 

    }

    return render(request, 'inbox.html',context)


@login_required(login_url='login')
def new_inbox_view(request):
    profile = request.user.profile
    messagesRequests = profile.messages.all()
    unreadCount = messagesRequests.filter(is_read=False).count()
    context = {
        'messagesRequests':messagesRequests ,
        'unreadCount':unreadCount, 

    }

    return render(request, 'new_inbox.html',context)

@login_required(login_url='login')



def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(pk=pk)
    if message.is_read == False:
        message.is_read == True
        message.save()
    context = {
        'message':message
    }
    return render(request,'message.html',context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('index')

    context = {'recipient': recipient, 'form': form}
    return render(request, 'message_form.html', context)
