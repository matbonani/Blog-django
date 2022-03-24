from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

