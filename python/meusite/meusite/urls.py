
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("enquete/", incluse("enquete.urls")),
    path("admin/", admin.site.urls),
]
