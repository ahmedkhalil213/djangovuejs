from django.urls import path
from .views import PDLCreateAPIView

urlpatterns = [
    path('create_pdl/', PDLCreateAPIView.as_view(), name='create_pdl'),
]