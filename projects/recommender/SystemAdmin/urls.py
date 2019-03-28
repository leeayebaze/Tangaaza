from django.urls import path
from . import views

app_name = 'SystemAdmin'
urlpatterns =[
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
]














