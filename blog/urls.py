from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('membros.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django.contrib.auth.urls = Dir prescisa se chamar Registrarion para ter acessos as View login/logout
