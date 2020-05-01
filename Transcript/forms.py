from django import forms

from .models import Transcript
class TranscriptForm(forms.ModelForm):
    class Meta:
        model = Transcript
    
        # fields = '__all__'
        fields = ["student","reason", "marksheet12", "marksheet34",
                  "marksheet56", "marksheet78", "feerecipt", "application"]
        exclude = ("student",)
        widgets = {
            'reason': forms.TextInput(attrs={'class': 'form-group'}),
            'marksheet12': forms.FileInput(attrs={'class': "form-group"}),
            'marksheet34': forms.FileInput(attrs={'class': 'form-group'}),
            'marksheet56': forms.FileInput(attrs={'class': 'form-group'}),
            'marksheet78': forms.FileInput(attrs={'class': 'form-group'}),
            'feerecipt': forms.FileInput(attrs={'class': 'form-group'}),
            'application': forms.FileInput(attrs={'class': 'form-group'}),
            }
    # def __init__(self, *args, **kwargs):
    #     super(TranscriptForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'