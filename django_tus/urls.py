from django.urls import path

from .views import TusUpload

urlpatterns = [
    path('upload/', TusUpload.as_view(), name='tus_upload'),
    path('upload/<uuid:resource_id>', TusUpload.as_view(), name='tus_upload_chunks'),
]
