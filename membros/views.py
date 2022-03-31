from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy('index')
    success_url = reverse_lazy('pasword_sucess')
    template_name = 'registration/change-password.html'


def password_sucess(request):
    return render(request, 'registration/password_sucess.html', {})
