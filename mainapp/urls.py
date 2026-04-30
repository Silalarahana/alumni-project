from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail'),
    path('alumni/edit/<int:id>/', views.edit_alumni, name='edit_alumni'),  # ← only once
    path('delete/<int:id>/', views.delete_alumni, name='delete_alumni'),

    path('notifications/', views.notifications, name='notifications'),
    path('notification/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notification/edit/<int:pk>/', views.edit_notification, name='edit_notification'),
    path('notification/delete/<int:pk>/', views.delete_notification, name='delete_notification'),

    path('placements/', views.placements, name='placements'),
    path('add_alumni/', views.add_alumni, name='add_alumni'),
    path('add-notification/', views.add_notification, name='add_notification'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('hod-dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('contact/', views.contact, name='contact'),
    path('departments/add/', views.add_department, name='add_department'),
    path('about-portal/', views.about_portal, name='about_portal'),
    path('export-alumni/', views.export_alumni_csv, name='export_alumni_csv'),
    path('view-id-card/<int:id>/', views.view_id_card, name='view_id_card'),
]