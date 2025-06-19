from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from. forms import ProfileForm,Level1ProfileForm,Level2ProfileForm,Level3ProfileForm,CompanyProfileForm,MessageForm
from . models import Level1Profile,Level2Profile,Level3Profile, CompanyProfile,Message,Profile,Address,Skill,Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
#location fields
import json
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q

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
    with open(settings.BASE_DIR / 'static' / 'rwandaState.json') as f:
        address_data = json.load(f)

    if request.method == 'POST':
        form = Level1ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # ✅ 1. Read selected address values
            province = request.POST.get('province')
            district = request.POST.get('district')
            sector = request.POST.get('sector')
            cell = request.POST.get('cell')
            village = request.POST.get('village')

            # ✅ 2. Create or get Address instance
            address, created = Address.objects.get_or_create(
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village
            )

            # ✅ 3. Save profile with that address
            level1_profile = form.save(commit=False)
            level1_profile.user = request.user
            level1_profile.address = address  # <- this is crucial
            level1_profile.save()
            form.save_m2m()  # for skills

            return redirect('index')  # or wherever
    else:
        form = Level1ProfileForm()

    return render(request, 'users/level1.html', {
        'form': form,
        'address_json': json.dumps(address_data)
    })



# Level2

def level2_dashboard(request):
    with open(settings.BASE_DIR / 'static' / 'rwandaState.json') as f:
        address_data = json.load(f)

    if request.method == 'POST':
        form = Level2ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # ✅ 1. Read selected address values
            province = request.POST.get('province')
            district = request.POST.get('district')
            sector = request.POST.get('sector')
            cell = request.POST.get('cell')
            village = request.POST.get('village')

            # ✅ 2. Create or get Address instance
            address, created = Address.objects.get_or_create(
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village
            )

            # ✅ 3. Save profile with that address
            level2_profile = form.save(commit=False)
            level2_profile.user = request.user
            level2_profile.address = address  # <- this is crucial
            level2_profile.save()
            form.save_m2m()  # for skills

            return redirect('home')  # or wherever
    else:
        form = Level2ProfileForm()

    return render(request, 'users/level2.html', {
        'form': form,
        'address_json': json.dumps(address_data)
    })

# def level2_dashboard(request):
#     if request.method == 'POST':
#         form = Level2ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             level2_profile = form.save(commit=False)
#             level2_profile.user= request.user
#             level2_profile.save()
#             return redirect('index')
#     else:
#         form = Level2ProfileForm()  

#     return render(request, 'users/level2.html', {'form': form})

# Level3
def level3_dashboard(request):
    with open(settings.BASE_DIR / 'static' / 'rwandaState.json') as f:
        address_data = json.load(f)

    if request.method == 'POST':
        form = Level3ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # ✅ 1. Read selected address values
            province = request.POST.get('province')
            district = request.POST.get('district')
            sector = request.POST.get('sector')
            cell = request.POST.get('cell')
            village = request.POST.get('village')

            # ✅ 2. Create or get Address instance
            address, created = Address.objects.get_or_create(
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village
            )

            # ✅ 3. Save profile with that address
            level3_profile = form.save(commit=False)
            level3_profile.user = request.user
            level3_profile.address = address  # <- this is crucial
            level3_profile.save()
            form.save_m2m()  # for skills

            return redirect('home')  # or wherever
    else:
        form = Level3ProfileForm()

    return render(request, 'users/level3.html', {
        'form': form,
        'address_json': json.dumps(address_data)
    })

# def level3_dashboard(request):
#     if request.method == 'POST':
#         form = Level3ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             level3_profile = form.save(commit=False)
#             level3_profile.user = request.user
#             level3_profile.save()
#             return redirect('index')

#     else:
#          form = Level3ProfileForm()
  
   
#     return render(request, 'users/level3.html',{'form':form})


# Company
def company_dashboard(request):
    with open(settings.BASE_DIR / 'static' / 'rwandaState.json') as f:
        address_data = json.load(f)

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Step 1: Extract address values
            province = request.POST.get('province')
            district = request.POST.get('district')
            sector = request.POST.get('sector')
            cell = request.POST.get('cell')
            village = request.POST.get('village')

            # Step 2: Get or create the address
            address, created = Address.objects.get_or_create(
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village
            )

            # Step 3: Save profile with address
            company_profile = form.save(commit=False)
            company_profile.user = request.user
            company_profile.address = address
            company_profile.save()

            return redirect('index')  # Or wherever you'd like
    else:
        form = CompanyProfileForm()

    return render(request, 'users/company.html', {
        'form': form,
        'address_json': json.dumps(address_data)
    })


# def company_dashboard(request):
#     if request.method == 'POST':
#         form = CompanyProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             company_profile = form.save(commit=False)
#             company_profile.user = request.user
#             company_profile.save()
#             return redirect('index')
#     else:

#         form =  CompanyProfileForm()
    
    
#     return render(request, 'users/company.html',{'form':form})


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

def appoitment_view(request):
    return render(request,'appoitment.html')
def market_place_view(request):
    return render(request,'market_place.html')

def allprofiles2_view(request):
    profiles2_list = Level2Profile.objects.all()
    paginator = Paginator(profiles2_list,8)
    page_number = request.GET.get('page')
    profiles2 = paginator.get_page(page_number)

    context = {
        'profiles2':profiles2
    }
    return render(request,'allprofile2.html',context)

# Profile details

@login_required
def level2_profile_detail(request, pk):
    profile = get_object_or_404(Level2Profile, pk=pk)

    if request.method == 'POST' and request.user == profile.user:
        form = Level2ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('level2_profile_detail', pk=pk)
    else:
        form = Level2ProfileForm(instance=profile) if request.user == profile.user else None

    return render(request, 'level2_profile_detail.html', {
        'profile': profile,
        'form': form
    })


#Company profiles
def allcompanyprofiles_view(request):
    companies_list =  CompanyProfile.objects.all()
    paginator = Paginator(companies_list,6)
    page_number = request.GET.get('page')
    companies = paginator.get_page(page_number)

    context = {
        'companies':companies
    }
    return render(request,'allcompanyprofiles.html',context)

def allprofiles3_view(request):
    profiles3_list = Level3Profile.objects.all()
    paginator = Paginator(profiles3_list,8)
    page_number = request.GET.get('page')
    profiles3 = paginator.get_page(page_number)

    context = {
        'profiles3':profiles3
    }
    return render(request,'allprofile3.html',context)

def allprofiles1_view(request):
    query = request.GET.get('q')  # global search
    location = request.GET.get('location')
    skill = request.GET.get('skill')
    category = request.GET.get('category')

    profiles1_list = Level1Profile.objects.all()

    if query:
        profiles1_list = profiles1_list.filter(
            Q(user__username__icontains=query) |
            Q(phone__icontains=query) |
            Q(skills__name__icontains=query) |
            Q(address__province__icontains=query) |
            Q(address__district__icontains=query) |
            Q(address__cell__icontains=query) |
            Q(address__village__icontains=query)
        ).distinct()

    if location:
        profiles1_list = profiles1_list.filter(
            Q(address__province__icontains=location) |
            Q(address__district__icontains=location) |
            Q(address__cell__icontains=location) |
            Q(address__village__icontains=location)
        ).distinct()

    if skill:
        profiles1_list = profiles1_list.filter(skills__name__icontains=skill).distinct()

    if category:
        profiles1_list = profiles1_list.filter(skills__category__name__icontains=category).distinct()

     # Form logic for the logged-in user's profile
    try:
        user_profile = Level1Profile.objects.get(user=request.user)
    except Level1Profile.DoesNotExist:
        user_profile = None

    if request.method == 'POST' and user_profile:
        form = Level1ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('allprofiles1')  # reload the page after saving
    else:
        form = Level1ProfileForm(instance=user_profile) if user_profile else None

    # Pagination
    paginator = Paginator(profiles1_list, 6)
    page_number = request.GET.get('page')
    profiles1 = paginator.get_page(page_number)

    # Pass filter options to the template
    categories = Category.objects.all()
    skills = Skill.objects.all()

    context = {
        'profiles1': profiles1,
        'query': query,
        'categories': categories,
        'skills': skills,
        'form':form,
    }

    return render(request, 'allprofile1.html', context)


    

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










