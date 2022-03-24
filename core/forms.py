from django import forms

from.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'titulo', 'body')

        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'body')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }