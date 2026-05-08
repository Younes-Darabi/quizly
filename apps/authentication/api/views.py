from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'detail':'User created successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    pass


class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message':'Hello World'})