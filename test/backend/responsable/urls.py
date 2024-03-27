from django.urls import path
from .views import ResponsableCreateView

urlpatterns = [
    path('commerciaux/', ResponsableCreateView.as_view(), name='commerciaux'),
]