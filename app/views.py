from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Url
from app.serializers import UrlSerializer


def get_ip_anonymous_user(request):
    user_ip = request.META.get("HTTP_X_FORWARDED_FOR")
    if user_ip is not None:
        ip = user_ip.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


@api_view(["GET", "POST"])
def url_lis(request):

    if request.method == "GET":
        if request.user.is_anonymous:
            url_list = Url.objects.filter(user=get_ip_anonymous_user(request)).filter(status=True)
            serializer = UrlSerializer(url_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        url_list = Url.objects.filter(user=request.user.id).filter(status=True)
        serializer = UrlSerializer(url_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_anonymous:
                serializer.save(user=get_ip_anonymous_user(request))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save(user=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def url_detail(request, pk):
    try:
        url = Url.objects.get(pk=pk)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UrlSerializer(url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        url.status = False
        url.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UrlView(APIView):
    def get(self, request, hash_):
        url = Url.objects.get(url_hash=hash_)
        url.clicked()

        return HttpResponseRedirect(url.url)
