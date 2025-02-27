from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('index/', views.index_view, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('level1/', views.level1_dashboard, name='level1_dashboard'),
    path('level2/', views.level2_dashboard, name='level2_dashboard'),
    path('level3/', views.level3_dashboard, name='level3_dashboard'),
    path('company/', views.company_dashboard, name='company_dashboard'),

    path('profile_user/',views.user_profile_view,name='profile'),
    path('profile1/',views.profile1_view,name='profile1'),
    path('profile2/',views.profile2_view,name='profile2'),
    path('profile3/',views.profile3_view,name='profile3'),
    path('profile_company/',views.company_profile_view,name='company-profile'),
    path('allprofile2/',views.allprofiles2_view,name='allprofiles2'),
    path('allcompanyprofiles/',views.allcompanyprofiles_view,name='allcompanyprofiles'),
    path('allprofile3/',views.allprofiles3_view,name='allprofiles3'),
    path('allprofile1/',views.allprofiles1_view,name='allprofiles1'),


]
