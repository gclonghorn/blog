from rest_framework import serializers
from post.models import Post, PostCategory
from user.models import User





class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')

#用于搜索结果展示博文概要
class PostSerializer(serializers.ModelSerializer):
    author = UserSrializer()

    class Meta:
        model = Post
        fields = ("title","author","pub_date","id","body")

class CategorySrializer(serializers.ModelSerializer):
    #posts=PostSerializer(many= True)

    class Meta:
        model = PostCategory
        fields = ("name","id",)#"posts"

#用于增删改博文
class CategorySrializer2(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ("id",)


#用于增删改博文
class PostEditSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    #category=CategorySrializer2()
    class Meta:
        model = Post
        fields = ('title','body','author','category','id','image','file','pub_date')


