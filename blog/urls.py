from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('membros.urls')),
]

# django.contrib.auth.urls = Dir prescisa se chamar Registrarion para ter acessos as View login/logout
