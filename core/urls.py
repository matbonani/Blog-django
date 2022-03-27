from django.urls import path
from .views import IndexView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artigo/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/', AddPostView.as_view(), name='add_post'),
    path('artigo/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('artigo/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
