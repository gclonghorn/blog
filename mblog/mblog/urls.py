from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from browse.views import PostListSet, CategoryViewset,RecommendListSet
from comments.views import CommentViewset,LikeViewset
from File.views import FileViewset
from post.views import PostEditViewset
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from user.views import UserViewset,UserFavViewSet
from.settings import MEDIA_ROOT
from django.views.static import serve


router=DefaultRouter()
#配置postsurl
router.register(r'list', PostListSet,basename="list")
#配置category的ur
router.register(r'category', CategoryViewset,basename="category")
#评论
router.register(r'comment', CommentViewset,basename="comment")
#点赞
router.register(r'like', LikeViewset,basename="like")
#用户
router.register(r'users', UserViewset)
#编辑博文
router.register(r'edit',PostEditViewset)
#用户关注
router.register(r'userfavs', UserFavViewSet)
#资源上传
router.register(r'files', FileViewset)
#首页推荐
router.register(r'recommend', RecommendListSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title="BAblog")),
    url(r'^', include(router.urls)),
    path('jwt-auth/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),  # drf 认证url
    path('api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('index/', TemplateView.as_view(template_name='index.html')),
      # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/upload/(?P<path>.*)', serve, {"document_root": 'media/upload/'}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': 'media/upload/', 'show_indexes':True}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
