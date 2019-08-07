
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


from . import serializers
from . import models
from . import permissions

"""Create your views here."""


class HelloApiView(APIView):
    """Test API view."""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features."""

        an_apiview = [
            'Uses a HTTP methods like GET, POST, PUT, PATCH and DELTE',
            'It is a traditional logic',
            'Gives you most control ovee a logic'
            'It is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        """Validate the serialiser"""
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Hanlde the update method"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """patch methods: only update provided fields"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """to delete a object"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message."""

        a_viewset = [
            'Uses a HTTP methods like GET, POST, PUT, PATCH and DELETE',
            'It is a traditional logic',
            'Gives you most control ovee a logic'
            'It is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)

        """Validate the serialiser"""
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Hanlde the get object by it is ID"""

        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """handle a update object"""

        return Response({'method': 'PUT'})

    def partial_update(self, request, pk= None):
        """handle only required objects"""

        return Response({'method': 'PATCH'})


    def destroy(self, request, pk=None):
        """to delete a object"""

        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    """That's how we add authentication and permission to endpoint apis"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    """Add filter option in user profile. Add filet_backends"""

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """Check email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profile feed item"""

    """Add Authentication class"""
    """put ',' TokenAuthentication : So Django knows it's Tuple"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()


    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)




