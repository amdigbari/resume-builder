from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="obtain_token_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
]
