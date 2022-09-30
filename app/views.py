from django.http import HttpResponseRedirect
from rest_framework import viewsets, mixins
from rest_framework.views import APIView

from app.models import Url
from app.serializers import UrlSerializer


class UrlViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlView(APIView):
    def get(self, request, hash_):
        url = Url.objects.get(url_hash=hash_)
        url.clicked()

        return HttpResponseRedirect(url.url)
