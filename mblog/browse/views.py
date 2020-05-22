
from post.models import Post,PostCategory
from .serializers import PostDetailSerializer,PostSerializer,CategorySrializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .filters import PostsFilter
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
    博客列表 搜索 分类 排序 分页
    retrieve:
    查看博文详情
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend)
    filter_class = PostsFilter
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
    分类列表
    retrieve:
    查看分类详情
    """
    queryset = PostCategory.objects.all()
    serializer_class = CategorySrializer




