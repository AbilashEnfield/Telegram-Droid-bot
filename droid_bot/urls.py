from django.urls import path
from . import views


urlpatterns = [
    path('', views.botChatData, name='bot'),
    path('activate/', views.trigger, name='activate')
]
