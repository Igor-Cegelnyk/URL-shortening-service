from django.urls import path, re_path
from rest_framework.authtoken import views

from app.views import url_lis, UrlView


urlpatterns = [
    path("api/", url_lis),
    path("api-token-auth/", views.obtain_auth_token),
    re_path(r"^redirect/(?P<hash_>.+)$", UrlView.as_view()),

]


app_name = "app"
