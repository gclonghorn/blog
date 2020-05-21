from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import Comment
from .serializers import CommentSerializer,LikeSerializer
# Create your views here.
class CommentViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """"
    create:
    创建评论
    destroy:
    删除评论
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewset( mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    create:点赞
    destroy:取消点赞
    """
    queryset = Comment.objects.all()
    serializer_class = LikeSerializer