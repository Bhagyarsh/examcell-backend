# api/urls.py
from django.urls import include, path

from .views import (dashboardview, examform, noticelist, payment,
                    transciptApplication, noticedetail, transciptstatus,
                    profiledetail, profileupdate, profileupdatestatus)
app_name = 'academic'
urlpatterns = [
    path('dashboard', dashboardview,name = "dashboard"),
    path('examform', examform,name = "examform"),
    path('notice', noticelist,name = "noticelist"),
    path('payment', payment,name = "payment"),
    path('notice/detail', noticedetail,name = "noticedetail"),
    path('profile/update', profileupdate,name = "profileupdate"),
    path('profile/status', profileupdatestatus,name = "profilestatus"),
    path('transcipt/Application', transciptApplication,name = "transciptApplication"),
    path('transcipt/Status', transciptstatus,name="transciptStatus"),
    path('profile/detail', profiledetail,name="profiledetail"),
]
