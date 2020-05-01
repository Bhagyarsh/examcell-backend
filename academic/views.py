from django.shortcuts import render
from Transcript.models import Transcript

def dashboardview(request):
    return render(request,'main/dashboard.html')





def payment(request):
    return render(request,'main/payment.html')


def profileupdatestatus(request):
    return render(request,'main/ProfileUpdateStatus.html')



def profiledetail(request):
    return render(request,'main/profileDetail.html')