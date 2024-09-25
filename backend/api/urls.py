from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUserView, ProfileDetailView

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),  # Login, logout, password reset
    path(
        "auth/registration/", include("dj_rest_auth.registration.urls")
    ),  # Registration
    path("auth/social/", include("allauth.socialaccount.urls")),  # Social login
    path("profile/", ProfileDetailView.as_view(), name="profile-detail"),  # for DRF
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
