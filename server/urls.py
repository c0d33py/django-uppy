from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', DemoClientView.as_view(), name='demo_client'),
    path('upload/', FileUpload),
    path('admin/', admin.site.urls),
    path('tus/', include('django_tus.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
