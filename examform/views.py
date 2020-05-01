from django.shortcuts import render
from .models import examform ,examformFill
from academic.models import klass
from academic.models import ktclass
from academic.models import student
from .forms import ExamForm
# Create your views here.


def examformlist(request):
    user = request.user
    try:
        stdobj = student.objects.get(user=user)
    except student.DoesNotExist:
        stdobj = None
    if stdobj:
        klsobj = stdobj.enrolledclass
        ktclsobj = ktclass.objects.filter(student=stdobj)
        examformobj = examform.objects.filter(klass=klsobj)
        formlist = []
        for kt in ktclsobj:
            ktform = examform.objects.filter(ktclass=kt)
        for form in examformobj:
            formlist.append(form)
        for form in ktform:
            formlist.append(form)
        print(formlist)
        context = {'formlist': formlist}
    return render(request, 'main/examFormlist.html',context)

def examformstatus(request,slug):
    Form = ExamForm()
    user = request.user
    try:
        stdobj = student.objects.get(user=user)
    except student.DoesNotExist:
        stdobj = None
    if stdobj:
        
        obj = examform.objects.get(slug=slug)
        try :
            examformFill.objects.get(student=stdobj)
            context = {"title":" Exam Form","pa":"This exam form already filled"}

            return render(request,'main/notther.html',context)
        except:
            klass = obj.klass
            ktclass =obj.ktclass
            sem = obj.sem
            added_on = obj.added_on
            open_till = obj.open_till
            addedby = obj.addedby
            is_kt = obj.is_kt
            fee = obj.fee
            examForm = ExamForm(request.POST,request.FILES)
            if examForm.is_valid():
                my_model = examformFill()
                my_model.examform = obj
                my_model.pervioushalltickit_no = examForm.cleaned_data.get('pervioushalltickit_no', None)
                my_model.feerecipt = examForm.cleaned_data.get('feerecipt', None)
                my_model.student = stdobj
                my_model.filled = True
                my_model.save()
            if klass:
                context = {"kclass":klass,"sem":sem,"added_on":added_on,"open_till":open_till,"is_kt":is_kt
                ,"fee":fee,"form":Form}
            else:
                context = {"kclass":ktclass,"sem":sem,"added_on":added_on,"open_till":open_till,"is_kt":is_kt
                ,"fee":fee,"form":Form}
        return render(request,'main/examFormwithinfo.html',context)
