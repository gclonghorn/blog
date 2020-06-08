from rest_framework import viewsets
from rest_framework import mixins
from .models import Comment,Like
from .serializers import CommentSerializer,LikeSerializer
from  rest_framework import authentication
from post.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        self.queryset = Comment.objects.filter(author=self.request.user)
        return self.queryset


class LikeViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    List:用户点赞列表
    create:点赞
    destroy:取消点赞
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_queryset(self):
        self.queryset = Like.objects.filter(author=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        instance=serializer.save()
        post = instance.post
        post.like_num += 1
        post.save()

    def perform_destroy(self, instance):
        post = instance.post
        post.like_num -= 1
        post.save()
        instance.delete()




