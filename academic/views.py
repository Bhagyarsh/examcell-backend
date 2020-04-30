from django.shortcuts import render

# Create your views here.
def dashboardview(request):
    return render(request,'main/dashboard.html')

def examform(request):
    return render(request,'main/examForm.html')

def noticelist(request):
    return render(request,'main/NoticesList.html')

def noticedetail(request):
    return render(request,'main/noticeDetail.html')

def payment(request):
    return render(request,'main/payment.html')

def profileupdate(request):
    return render(request,'main/updateProfile.html')

def profileupdatestatus(request):
    return render(request,'main/ProfileUpdateStatus.html')

def transciptApplication(request):
    return render(request,'main/transcriptApp.html')

def transciptstatus(request):
    return render(request,'main/TranscriptStatus.html')

def profiledetail(request):
    return render(request,'main/profileDetail.html')