# api/urls.py
from django.urls import include, path

from .views import NoticeListApiView
urlpatterns = [

#    path('auth/jwt', AuthAPIView.as_view()),
    path('notices', NoticeListApiView.as_view()),
]
