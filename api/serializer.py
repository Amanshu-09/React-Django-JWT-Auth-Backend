from rest_framework.serializers import ModelSerializer
from api.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'address']