# api/urls.py
from django.urls import include, path

from .views import (dashboardview, payment,
                      profileupdatestatus)
app_name = 'academic'
urlpatterns = [
    path('dashboard', dashboardview,name = "dashboard"),
    # path('examform', examform,name = "examform"),
    path('payment', payment,name = "payment"),# "{% url 'academic:transciptApplication' %}"
    path('profile/status', profileupdatestatus,name = "profilestatus"),

   
]
