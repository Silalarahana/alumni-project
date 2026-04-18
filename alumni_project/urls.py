from django.contrib import admin
from django.urls import path, include
from mainapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('alumni/', views.alumni_list, name='alumni_list'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail'),

    path('notifications/', views.notifications, name='notification_list'),   

    path('hod/', views.hod_add_alumni, name='hod_add_alumni'),
    path('hod-dashboard/', views.hod_dashboard, name='hod_dashboard'),

    path('notification/<int:pk>/', views.notification_detail, name='notification_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('', include('mainapp.urls')),
]