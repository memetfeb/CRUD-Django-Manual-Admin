from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tindak_pidana/', include('tindak_pidana.urls')),
    path('', include('tindak_pidana.urls')),
]
