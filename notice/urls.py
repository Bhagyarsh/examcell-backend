# api/urls.py
from django.urls import include, path

from .views import ( noticelistview,
                     noticeDetailview)
app_name = 'notice'
urlpatterns = [
    path('notice/list', noticelistview,name = "noticelist"),
    path('notice/detail/<slug:slug>', noticeDetailview,name = "noticedetail"),
]
