from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView ,CreateView
from .models import Verifiy_email
from .forms import UserEmailChangeForm,RegisterFormSession
from django.urls import reverse_lazy

class CreateUser(CreateView):
    form_class = RegisterFormSession
    template_name = 'auth/login.html'
    success_url = '/admin'


def changedemailview(request):
    return render(request, 'verify_email.html')
def emailverifedview(request, slug, key):
    Verified_email_obj = get_object_or_404(Verifie_email, slug=slug, key=key)
    user = Verified_email_obj.user
    if user.Verified == False:
        print("user found")
        user.Verified = True
        user.save()
        Verified_email_obj.delete()
    print("user found")
    return render(request, 'verify_email.html')


class EmailChangeView(FormView):
    form_class = UserEmailChangeForm
    template_name = 'forms.html'
    success_url = reverse_lazy('changed_email')

    # def get_initial(self):
    #     initial = super(EmailChangeView, self).get_initial()
    #     if self.request.user.is_authenticated:
    #         initial.update({'name': self.request.user.get_full_name()})
    #     return initial

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(EmailChangeView, self).form_valid(form)

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)