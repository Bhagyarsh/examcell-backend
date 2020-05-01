from django.shortcuts import render

# Create your views here.
from academic.models import student
from .models import notice
def noticelistview(request):
    user = request.user
    stdobj = student.objects.get(user=user)
    kclss = student.enrolledclass
    noticelist = []
    notobj = notice.objects.all()
    if notobj:
        for noti in notobj:
            if kclss in noti.displaytoclasses.all():
                noticelist.append(noti)
            if noti.displaytoall:
                noticelist.append(noti)
    context = {"noticelist":noticelist}
    return render(request,'main/NoticesList.html',context)


def noticeDetailview(request,slug):
    notobj = notice.objects.get(slug=slug)
    return render(request,'main/noticeDetail.html',{"notice":notobj})