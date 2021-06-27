from django.urls import path
from . import views


#test comment 

urlpatterns = [
    path('', views.default, name='redirect_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classroom/', views.classroom, name='classroom'),
    path('announcements/', views.announcements, name='announcements'),
    path('resources/', views.resources, name='resources'),

    #functionality
    path('video_feed', views.video_feed, name='video_feed'),
    path('save_notes', views.save_notes, name='save_notes'),

    path('chat_function', views.chat_function, name='chat_function'),
    path('chat_messages', views.chat_messages, name='chat_messages'),
]