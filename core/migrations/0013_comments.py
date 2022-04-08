# Generated by Django 3.2 on 2022-04-06 19:24

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_profile_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('hora', models.TimeField(auto_now=True, verbose_name='horario')),
                ('body', models.TextField()),
                ('autor', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]