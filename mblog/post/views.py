from rest_framework import viewsets
from rest_framework import mixins
from .models import Post
from .serializers import PostEditSerializer

class PostEditViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
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