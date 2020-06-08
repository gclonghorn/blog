from rest_framework import viewsets
from rest_framework import mixins
from .models import Post
from .serializers import PostEditSerializer
from  rest_framework import authentication
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.conf import settings

from mblog.settings import MEDIA_ROOT
import os
class PostEditViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """"
    create:
    创建博文
    destroy:
    删除博文
    update:
    更新博文
    """
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)  # authentication.SessionAuthentication

    def get_queryset(self):
        self.queryset= Post.objects.filter(author=self.request.user)
        return self.queryset


