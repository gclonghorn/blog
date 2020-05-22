from rest_framework.routers import DefaultRouter
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from browse.views import PostListSet, CategoryViewset
from comments.views import CommentViewset,LikeViewset
from post.views import PostEditViewset
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from user.views import UserViewset
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
router.register(r'user', UserViewset)
#编辑博文
router.register(r'edit',PostEditViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title="BAblog")),
    url(r'^', include(router.urls)),
    path('jwt-auth/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),  # drf 认证url
    path('api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),

]
