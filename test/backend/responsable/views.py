from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ResponsableSerializer

class ResponsableCreateView(generics.CreateAPIView):
    serializer_class = ResponsableSerializer

    def create(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Responsable details validated and saved successfully."}, status=status.HTTP_200_OK)