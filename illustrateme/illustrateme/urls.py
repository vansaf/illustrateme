from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chlidren_workshops/', include('children_workshops.urls')),
    path('adult_workshops/', include('adult_workshops.urls')),
]