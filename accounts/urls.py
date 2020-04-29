# api/urls.py
from django.urls import  path,include
from . import views
urlpatterns = [
    path('user/email/verify/<slug:slug>/<str:key>/', views.emailverifedview,name='verifed email'),
    path('User/email/change', views.EmailChangeView.as_view(),name='email changed'),
    path('User/update/email', views.changedemailview,name='changed_email'),
    path('login', views.CreateUser.as_view(),name='login'),
    path('api/v1/',include("accounts.api.jwt.urls")),


]
