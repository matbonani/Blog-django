from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from stdimage import StdImageField


class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    atualizacao = models.DateField('Atualização', auto_now='True')
    hora = models.TimeField('horario', auto_now=True)

    class Meta:
        abstract = True


class Profile(Base):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = StdImageField(null=True, blank=True, upload_to='images/profile')
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Post(Base):
    titulo = models.CharField('Título', max_length=255)
    header_title = StdImageField(null=True, blank=True, upload_to='images/')
    autor = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    body = RichTextField('Post', blank=True, null=True)
    # body = models.TextField()
    snippet = models.CharField('Sobre oque é ?', max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)


class Comments(Base):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    body = models.TextField('Comentário')

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.autor)

