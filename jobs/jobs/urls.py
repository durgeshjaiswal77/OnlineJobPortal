from django.contrib import admin
from django.urls import path, include

#from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
]
