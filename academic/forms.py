from django import forms

from .models import studenteditprofilerequest
    # clgregisterid = models.CharField(max_length=16)
    # user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # enrolledclass = models.OneToOneField(to=klass, on_delete=models.CASCADE)
    # roll_no = models.IntegerField()
    # Department = models.CharField(max_length=20,blank=True,null=True)
    # div = models.CharField(max_length=10)
    # phone_no = models.IntegerField()
    # email_id = models.EmailField()
    # DOB = models.DateField()
    # address = models.CharField(max_length=250)
    # city = models.CharField(max_length=16)
    # pincode = models.IntegerField()
class studenteditprofilerequestForm(forms.ModelForm):
    class Meta:
        model = studenteditprofilerequest
        fields = "__all__"
        exclude = ("user","enrolledclass",)
        # widgets = {
        #     'clgregisterid': forms.TextInput(attrs={'class': 'form-group'}),
        #     'roll_no': forms.IntegerField(attrs={'class': "form-group"}),
        #     'Department': forms.TextInput(attrs={'class': 'form-group'}),
        #     'div': forms.TextInput(attrs={'class': 'form-group'}),
        #     'phone_no': forms.IntegerField(attrs={'class': 'form-group'}),
        #     'email_id': forms.FileInput(attrs={'class': 'form-group'}),
        #     'address': forms.TextField(attrs={'class': 'form-group'}),
        #     'city': forms.TextInput(attrs={'class': 'form-group'}),
        #     'pincode': forms.IntegerField(attrs={'class': 'form-group'}),
        #     }