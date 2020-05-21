
from post.models import Post
from .serializers import PostDetailSerializer,PostSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import  DjangoFilterBackend
import django_filters

class StandardResultsSetPagination(PageNumberPagination):
    """
    分页
    """
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class PostListSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    博客搜索列表
    retrieve:
    查看博文详情
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'body')
    ordering_fields = ('pub_date',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        elif self.action == "list":
            return PostSerializer
        return PostSerializer

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    博客分类列表
    retrieve:
    指定分类查看博客列表
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        elif self.action == "list":
            return PostSerializer
        return PostSerializer



