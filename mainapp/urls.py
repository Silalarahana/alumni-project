from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('placements/', views.placements, name='placements'),
    path('add-alumni/', views.add_alumni, name='add_alumni'),
    path('hod-login/', views.hod_login, name='hod_login'),
    path('hod-dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('contact/', views.contact, name='contact'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail'),
    path('edit/<int:id>/', views.edit_alumni, name='edit_alumni'),
    path('delete/<int:id>/', views.delete_alumni, name='delete_alumni'),
    path('alumni/<int:id>/', views.alumni_detail, name='alumni_detail')

]
