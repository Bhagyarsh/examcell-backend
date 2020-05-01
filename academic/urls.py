# api/urls.py
from django.urls import include, path

from .views import (dashboardview, noticelist, payment,
                     noticedetail, profileupdatestatus)
app_name = 'academic'
urlpatterns = [
    path('dashboard', dashboardview,name = "dashboard"),
    # path('examform', examform,name = "examform"),
    path('notice', noticelist,name = "noticelist"),
    path('payment', payment,name = "payment"),# "{% url 'academic:transciptApplication' %}"
    path('notice', noticelist,name = "noticedetail"),
    path('profile/status', profileupdatestatus,name = "profilestatus"),

   
]
