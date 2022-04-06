from django.urls import path
from . import views

from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView\
    , CreateProfilePageView

urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='registro'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_sucess', views.password_sucess, name='pasword_sucess'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),

]
