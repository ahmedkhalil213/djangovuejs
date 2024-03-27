from django.urls import path
from .views import EntrepriseCreateView
from .views import EntrepriseListView
from .views import EntrepriseDetailView,EntrepriseRetrieveFromSiret

urlpatterns = [
    path('entreprise/create/', EntrepriseCreateView.as_view(), name='entreprise-create'),
    path('entreprises/', EntrepriseListView.as_view(), name='entreprise-list'),
    path('entreprises/<int:pk>/', EntrepriseDetailView.as_view(), name='entreprise-detail'),
    path('entreprise/id/', EntrepriseRetrieveFromSiret.as_view(),name='entreprise-retrieve-from-siret'),

]
