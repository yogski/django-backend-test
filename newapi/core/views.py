from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Order
from rest_framework import views, viewsets, permissions
from rest_framework.response import Response
from core.serializers import UserSerializer, GroupSerializer, OrderSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    Allow CRUD actions to users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    Allow CRUD actions to Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    """
    Allow CRUD actions to Order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrivateView(views.APIView):
    """
    Example: Request-view-response with authentication
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        content = {'message': 'Hello, World! (Private)'}
        return Response(content)

class PublicView(views.APIView):
    """
    Example: Request-view-response with no authentication
    """
    def get(self, request):
        content = {'message': 'Hello, World! (Public)'}
        return Response(content)