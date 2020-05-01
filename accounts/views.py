from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView, CreateView
from .models import profile
from .forms import UserEmailChangeForm, RegisterFormSession
from django.urls import reverse_lazy
from academic.models import student, studenteditprofilerequest
from academic.forms import studenteditprofilerequestForm


def Profileupdateview(request):
    form = studenteditprofilerequestForm()
    stdObject = student.objects.get(user=request.user)
    try:
        spreq = studenteditprofilerequest.objects.get(user=request.user)
        if spreq.acknowledge:
            context = {"id":"1","addedat":spreq.addedat,"status":"acknowledge"}
        else:
            context = {"id":"1","addedat":spreq.addedat,"status":"pending"}
            print(context)
        return render(request,"main/ProfileUpdateStatus.html",context)
    except:
        if request.method == "POST":
            form = studenteditprofilerequestForm(request.POST)
            if form.is_valid():
                studenteditprofile = form.save(commit=False)
                studenteditprofile.user = request.user
                studenteditprofile.enrolledclass = stdObject.enrolledclass
                studenteditprofile.save()
            try:
                spreq = studenteditprofilerequest.objects.get(user=request.user)
                if spreq.acknowledge:
                    context = {"id":"1","addedat":spreq.addedat,"status":"acknowledge"}
                else:
                    context = {"id":"1","addedat":spreq.addedat,"status":"pending"}
                print(context)
                return render(request,"main/ProfileUpdateStatus.html",context)
            except:
                pass
        return render(request, "main/profileupdate.html", {'form': form})


def Profileupdatestatusview(request):
    try:
        spreq = studenteditprofilerequest.objects.get(user=request.user)
        if spreq.acknowledge:
            context = {"id":"1","addedat":spreq.addedat,"status":"acknowledge"}
        else:
            context = {"id":"1","addedat":spreq.addedat,"status":"pending"}
        print(context)
        return render(request,"main/ProfileUpdateStatus.html",context)
    except:  
        return render(request, "main/notther.html", {"title": "Nothing to show", "pa": "There is no Profile request give !"})
def profileDetailview(request):
    user = request.user
    probj = profile.objects.get(user=user)
    if probj.student:
        stuobj = student.objects.get(user=user)
        fullname = user.get_full_name()
        emailadd = stuobj.email_id
        DOB = stuobj.DOB
        phone_no = stuobj.phone_no
        Designation ='student'
        pincode = stuobj.pincode
        city = stuobj.city
        address = stuobj.address
        Department = stuobj.Department
    context = {'fullname':fullname,"emailadd":emailadd,
               'DOB':DOB,"phone_no":phone_no,"Designation": Designation,
               'pincode':pincode,"city":city,"address":address,"Department":Department}
    print(context)
    return render(request,"main/profileDetail.html",context)
