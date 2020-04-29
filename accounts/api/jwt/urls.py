# api/urls.py
from django.urls import include, path
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import AuthAPIView,RegisterAPIView
urlpatterns = [

#    path('auth/jwt', AuthAPIView.as_view()),
    path('auth/jwt/register', RegisterAPIView.as_view()),
    path('auth/jwt', obtain_jwt_token),
    path('auth/jwt/verify', verify_jwt_token),
    path('auth/jwt/refresh', refresh_jwt_token),
]
