from django.urls import path

from common.views import HomeView, ContactView
from common.api_endpoints import *

app_name = "common"

urlpatterns = [
    path("media/upload/", MediaFileCreateAPIView.as_view(), name="media-upload"),
    path("media/delete/", MediaFileDestroyAPIView.as_view(), name="media-delete"),

    path("index/", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
]
