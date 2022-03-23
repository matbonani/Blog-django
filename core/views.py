from django.views.generic import ListView, DetailView

from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'artigo_detail.html'
