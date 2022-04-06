from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from django.shortcuts import render, get_object_or_404

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from core.models import Profile


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


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args,  **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'facebook', 'twitter', 'instagram', 'linkedin']
    success_url = reverse_lazy('index')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    success_url = reverse_lazy('index')
    # fields = '__all__'


