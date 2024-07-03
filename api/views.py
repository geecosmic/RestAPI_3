
from rest_framework import generics, permissions
from .models import Members
from .serializers import MemberSerializers, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .permissions import IsPublicEndpoint, IsAuthenticatedEndpoint
from rest_framework import status 
from .permissions import IsOwner



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({'detail': 'Method "GET" not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




from rest_framework import generics

class MembersListCreate(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            # return [IsPublicEndpoint()]
            return [IsAuthenticatedEndpoint()]

        elif self.request.method == 'POST':
            return [IsAuthenticatedEndpoint()]
        else:
            return []  # No permissions required for other methods

    # Optionally, you can override other methods like `perform_create()` for custom create logic


class MembersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Members.objects.all()
    serializer_class = MemberSerializers
    lookup_field = "pk"






















