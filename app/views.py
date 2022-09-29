from rest_framework import viewsets

from app.models import Url


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = CinemaHallSerializer
