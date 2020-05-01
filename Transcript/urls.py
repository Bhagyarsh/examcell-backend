# api/urls.py
from django.urls import include, path

from .views import (transciptApplication, transciptstatus)
app_name = 'Transcript'
urlpatterns = [
    path('transcipt/Application', transciptApplication,name = "transciptApplication"),
    path('transcipt/Status', transciptstatus,name="transciptStatus"),
]
