from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.landing_page_view,name='landing-page'),
    path('home/',views.home_view,name='home'),
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
    #Profiles
    path('allprofile2/',views.allprofiles2_view,name='allprofiles2'),
    #Profile Details
    path('level2-profile/<int:pk>/', views.level2_profile_detail, name='level2_profile_detail'),
    path('allcompanyprofiles/',views.allcompanyprofiles_view,name='allcompanyprofiles'),
    path('allprofile3/',views.allprofiles3_view,name='allprofiles3'),
    path('allprofile1/',views.allprofiles1_view,name='allprofiles1'),
    path('like_profile/<int:profile_id>/', views.like_profile, name='like_profile'),
    path('like_level2/<int:profile_id>/', views.like_level2_profile, name='like_level2_profile'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('new_inbox/', views.new_inbox_view, name='new-inbox'),
    path('message/<str:pk>/', views.viewMessage, name='message'),
    path('create-message/<uuid:pk>/', views.createMessage, name='create-message'),
    path('chaining/', include("smart_selects.urls")),

    path('appoitment/',views.appoitment_view,name='appoitment'),
    path('superuser/',views.superuser_dashboard,name='superuser-dashboard'),
    path('subscription-plans/',views.subscription_plans_view,name='subscription-plans'),
     
   
    path('marketplace/', views.market_place_view, name='market-place'),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('export/excel/', views.export_users_excel, name='export_users_excel'),
    path('export/pdf/', views.export_users_pdf, name='export_users_pdf'),
    path('messages/mark-read/<uuid:pk>/', views.mark_message_read, name='mark_message_read'),
]