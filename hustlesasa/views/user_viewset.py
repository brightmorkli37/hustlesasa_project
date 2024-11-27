from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from hustlesasa.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """ Viewset for managing Users. """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Create user
    def create(self, request, *args, **kwargs):
        """
        Handle user creation explicitly to set a password.
        """

        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=data.get('password'),
            first_name=serializer.validated_data.get('first_name', ''),
            last_name=serializer.validated_data.get('last_name', ''),
            email=serializer.validated_data.get('email', '')
        )
        
        response_serializer = self.get_serializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

