from rest_framework import viewsets

from app.models import Url
from app.serializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
