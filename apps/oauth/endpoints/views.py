from rest_framework import viewsets, parsers, permissions

from .. import serializers

class UserViewSet(viewsets.ModelViewSet):
    """Update user profile
    """
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = (serializers.UserSerializer,)
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return self.request.user
    
    def get_object(self):
        return self.get_queryset()