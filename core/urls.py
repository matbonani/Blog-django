from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artigo/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
