from django import forms
from .models import examform


class ExamForm(forms.Form):
    pervioushalltickit_no = forms.CharField(max_length=40, required=True)
    feerecipt = forms.FileField()