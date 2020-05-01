from django.shortcuts import render,get_object_or_404
from .forms import TranscriptForm
from .models import Transcript
from django.contrib.auth import get_user_model
User = get_user_model()
from academic.models import student
def transciptApplication(request):
    forms = TranscriptForm()
    user = request.user
    try:
        stdobj = student.objects.get(user=user)

    except student.DoesNotExist:
        stdobj = None
    try:
        Transobj = Transcript.objects.get(student=stdobj)

    except Transcript.DoesNotExist:
        Transobj = None
    if Transobj:
        return render(request,'main/dashboard.html')
    if stdobj:
        print(user)
        print(stdobj)
     
        if request.method == "POST":
            form = TranscriptForm(request.POST,request.FILES)
            if form.is_valid():
                # print(form.student)
                transcript = form.save(commit=False)
                transcript.student =  stdobj
                transcript.save()
                return render(request,'main/TranscriptStatus.html')
            else:
                print(form.errors)
                print('ERROR')

    return render(request,'main/transcriptApp.html',{'form':forms})

def transciptstatus(request):
    user = request.user
    stdobj = student.objects.filter(user=user)
    if stdobj:
        try:
            Transobj = Transcript.objects.get(student=stdobj[0])
        except Transcript.DoesNotExist:
            return render(request, "main/notther.html", {"title": "Nothing to show", "pa": "There is no Transcript request give !"})
            
        print(Transobj)
        if Transobj:
            if not Transobj.status:
                context = {"Applied_at":Transobj.added_at,"status":'pending',"class":"text-danger"}
            else:
                context = {"Applied_at":Transobj.added_at,"status":'Success',"class":"text-success"}
            print(context)
        return render(request,'main/TranscriptStatus.html',context)