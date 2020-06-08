import django_filters
from post.models import Post
class PostsFilter(django_filters.rest_framework.FilterSet):
    """
    博文过滤类
    """
    category = django_filters.NumberFilter(method='category_filter') #外键所以是numberfilter，category命名看前端
    author =django_filters.NumberFilter(method='author_filter')

    def category_filter(self,queryset,name,value): #默认传递参数,value=category.id
       return queryset.filter(category_id=value)

    def author_filter(self,queryset,name,value):
        return queryset.filter(author_id=value)


    class Meta:
        model= Post
        fields = ['category','author']