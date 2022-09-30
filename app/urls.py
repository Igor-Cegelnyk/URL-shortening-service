from django.urls import path, re_path

from app.views import url_lis, UrlView, url_detail

urlpatterns = [
    path("api/", url_lis),
    path("api/<int:pk>/", url_detail),
    re_path(r"^redirect/(?P<hash_>.+)$", UrlView.as_view()),

]


app_name = "app"
