from django.urls import path,include
from .views import *

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', signup_user, name='signup'),
    path('', userDetail, name='user_detail'),
    path('delete/<int:pk>/', deleteUser, name='delete_user'),
    path('update/<int:pk>/', updateUser, name='update_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]