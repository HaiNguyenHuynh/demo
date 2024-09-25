from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", views.index, name="index"),
    path("<path:path>/", views.catch_all, name="index"),
]
