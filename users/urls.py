from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('level1/', views.level1_dashboard, name='level1_dashboard'),
    path('level2/', views.level2_dashboard, name='level2_dashboard'),
    path('level3/', views.level3_dashboard, name='level3_dashboard'),
    path('company/', views.company_dashboard, name='company_dashboard'),

]
