from rest_framework import serializers

from app.models import Url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ("id", "url", "short_url", "clicks", "time_click")
