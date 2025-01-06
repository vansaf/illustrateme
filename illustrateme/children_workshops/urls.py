from django.urls import path

from django.urls import path

from . import views

app_name = 'children'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]