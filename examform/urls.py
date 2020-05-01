# api/urls.py
from django.urls import include, path

from .views import examformlist , examformstatus
app_name = 'examForm'
urlpatterns = [
    path('examform/list', examformlist,name = "examformlist"),
    path('examform/form/<slug:slug>', examformstatus,name="examform"),
]
