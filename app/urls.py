from django.urls import path, include
from rest_framework import routers

from app.views import UrlViewSet

router = routers.DefaultRouter()
router.register("app", UrlViewSet)

urlpatterns = [path("", include(router.urls))]


app_name = "app"
