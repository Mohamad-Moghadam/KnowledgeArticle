from django.urls import path
from.views import SignUp
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("sign-up", SignUp.as_view(), name="user"),
    path("log-in", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh-login", TokenRefreshView.as_view(), name="token_refresh")
]
