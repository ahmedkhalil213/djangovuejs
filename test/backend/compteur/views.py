from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Compteur
from .serializers import CompteurSerializer
from rest_framework.permissions import IsAuthenticated
class PDLCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]
        serializer = CompteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "PDL created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)