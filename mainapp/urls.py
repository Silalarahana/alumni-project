from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('placements/', views.placements, name='placements'),
    path('add_alumni/', views.add_alumni, name='add_alumni'),
    path('login/', views.login_view, name='login'),
    path('hod-dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('contact/', views.contact, name='contact'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail'),
    path('edit/<int:id>/', views.edit_alumni, name='edit_alumni'),
    path('delete/<int:id>/', views.delete_alumni, name='delete_alumni'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('add-notification/', views.add_notification, name='add_notification'),
    path('logout/',views.logout_view,name='logout'),
    path('alumni/edit/<int:id>/', views.edit_alumni, name='edit_alumni'),
    path('departments/add/', views.add_department, name='add_department'),
    path('notification/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notification/edit/<int:pk>/', views.edit_notification, name='edit_notification'),
    path('notification/delete/<int:pk>/', views.delete_notification, name='delete_notification'),
    path('about-portal/', views.about_portal, name='about_portal'),

]