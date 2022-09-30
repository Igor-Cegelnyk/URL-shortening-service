from django.urls import path, include, re_path
from rest_framework import routers

from app.views import UrlViewSet, UrlView

router = routers.DefaultRouter()
router.register("api", UrlViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r"^redirect/(?P<hash_>.+)$", UrlView.as_view()),

]


app_name = "app"
