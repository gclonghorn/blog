from rest_framework import serializers
from post.models import Post, PostCategory
from user.models import User
from comments.serializers import CommentDetailSerializer,LikeDetailSerializer


class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ("name","id")


class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id")


class PostSerializer(serializers.ModelSerializer):
    author = UserSrializer()

    class Meta:
        model = Post
        fields = ("title","author","pub_date","id")


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSrializer()
    category = CategorySrializer()
    comments = CommentDetailSerializer(many=True, read_only=True)
    likes = LikeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title','body','pub_date','author','category','comments','likes')

