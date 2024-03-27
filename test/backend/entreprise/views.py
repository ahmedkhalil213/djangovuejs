from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Entreprise
from .serializers import EntrepriseCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Entreprise
from .serializers import *
from rest_framework.generics import RetrieveAPIView

class EntrepriseCreateView(generics.CreateAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseCreateSerializer

    def create(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Entreprise created successfully."}, status=status.HTTP_200_OK)



class CustomPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

class EntrepriseListView(generics.ListAPIView):
        queryset = Entreprise.objects.all()
        serializer_class = EntrepriseSerializer
        pagination_class = CustomPagination
        permission_classes = [IsAuthenticated]
class EntrepriseDetailView(RetrieveAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class EntrepriseRetrieveFromSiret(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SiretSerializer(data=request.data)
        if serializer.is_valid():
            siret = serializer.validated_data.get('siret')
            try:
                entreprise = Entreprise.objects.get(siret=siret)
                entreprise_id_serializer = EntrepriseIdSerializer(entreprise)
                return Response(entreprise_id_serializer.data, status=status.HTTP_200_OK)
            except Entreprise.DoesNotExist:
                return Response({"message": "Enterprise not found for the provided SIRET."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

