# api/urls.py
from django.urls import  path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    # path('user/email/verify/<slug:slug>/<str:key>/', views.emailverifedview,name='verifed email'),
    # path('User/email/change', views.EmailChangeView.as_view(),name='email changed'),
    # path('User/update/email', views.changedemailview,name='changed_email'),
    # path('login', views.CreateUser.as_view(),name='login'),
    path("signin",views.signin,name="login"),
    path("signup",views.signup,name="register"),
    path('api/v1/',include("accounts.api.jwt.urls")),
    path('profile/status',views.Profileupdatestatusview,name='profilestatus'),
    path('profile/update',views.Profileupdateview,name='profileupdate'),
    path('profile/detail',views.profileDetailview,name='profiledetail')

]
