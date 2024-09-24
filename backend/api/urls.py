from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUserView, ProfileDetailView

urlpatterns = [
    path("user/register/", RegisterUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("profile/", ProfileDetailView.as_view(), name="profile-detail"),  # for DRF
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
