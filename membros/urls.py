from django.urls import path
from . import views

from .views import UserRegisterView, UserEditView, PasswordsChangeView

urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='registro'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_sucess', views.password_sucess, name='pasword_sucess')

]
