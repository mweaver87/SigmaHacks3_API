from django.urls import path

from . import views

#test comment 

urlpatterns = [
    path('', views.default, name='redirect_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classroom/', views.classroom, name='classroom'),
    path('announcements/', views.announcements, name='announcements'),
    path('resources/', views.resources, name='resources'),
]