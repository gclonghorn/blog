from rest_framework import serializers
from post.models import Post, PostCategory
from user.models import User

class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ("name","id")


class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id")


#用于增删改博文
class PostEditSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title','body','pub_date','author','category','id',)


