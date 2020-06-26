from rest_framework import viewsets
from rest_framework import mixins
from .models import Post
from .serializers import *
from  rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from browse.views import StandardResultsSetPagination
from django.http import HttpResponse
from mblog.settings import MEDIA_ROOT
import os
class FileViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """"
    List：
    资源列表
    create:
    上传资源
    destroy:
    删除资源
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('author',)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)  # authentication.SessionAuthentication



