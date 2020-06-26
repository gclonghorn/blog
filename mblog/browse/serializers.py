from rest_framework import serializers
from post.models import Post, PostCategory
from user.models import User
from comments.models import Like
from comments.serializers import CommentDetailSerializer,LikeDetailSerializer
from post.serializers import CategorySrializer





class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')

#用于搜索结果展示博文概要
class PostSerializer(serializers.ModelSerializer):
    author = UserSrializer()
    category = CategorySrializer()
    class Meta:
        model = Post
        fields = ("title","author","pub_date","id","like_num",'read_num','excerpt','category')

#用于展示博文详情
class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSrializer()
    category = CategorySrializer()
    comments = CommentDetailSerializer(many=True, read_only=True)
    likes = LikeDetailSerializer(many=True, read_only=True)
    like_num = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title','body','pub_date','author','category','comments','likes',
                  'like_num','read_num','image','file','excerpt','id')

    def get_like_num(self,obj):
        like_num=len(Like.objects.filter(post=obj))
        return like_num

