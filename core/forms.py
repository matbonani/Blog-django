from django import forms

from.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'titulo', 'snippet', 'body', 'header_title')

        widgets = {
            # 'autor': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'snippet', 'body')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }