from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("reporting-app/", include("reportingApp.urls")),
    path("admin/", admin.site.urls),
]