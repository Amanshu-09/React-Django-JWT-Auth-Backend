from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Built in views
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.
User = get_user_model()

@api_view(['POST'])
def signup_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    print(data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Created !')
    print(serializer.errors)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetail(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User Deleted !')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response('User Updated !')
    print(serializer.errors)
    return Response(serializer.errors)