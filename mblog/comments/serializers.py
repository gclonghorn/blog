from rest_framework import serializers
from.models import Comment,Like
from user.models import User
from rest_framework.validators import UniqueTogetherValidator


#用于评论者概要信息
class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')

#序列化被回复评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    author=UserSrializer()
    class Meta:
       model = Comment
       fields = ("id", "author")  #若添加删除功能fields需包含“id"字段

#序列化子评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    author=UserSrializer()
    class Meta:
       model = Comment
       fields = ('id','author','body','pub_date')  #若添加删除功能fields需包含“id"字段


#用于增删评论
class CommentSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    #reply_comment = ReplyCommentSerializer()

    class Meta:
        model = Comment
        fields = ('id','author','post','body','reply_comment',)  #若添加删除功能fields需包含“id"字段

#用于博文详情页展示评论详情
class CommentDetailSerializer(serializers.ModelSerializer):

    reply_comment = ReplyCommentSerializer()
    author = UserSrializer()
    replies=ReplyCommentSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id','author','post','body','pub_date','reply_comment','replies')#reply_comment:回复的哪个  replies:有哪些回复

#用于博文详情页展示点赞者列表
class LikeDetailSerializer(serializers.ModelSerializer):
    author = UserSrializer()
    class Meta:
        model = Like
        fields = ('author','id')

#用于增删点赞
class LikeSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = ('author','post','pub_date','id')  #若添加删除功能fields需包含“id"字段
        validators = [
            UniqueTogetherValidator(queryset=Like.objects.all(), fields=('author', 'post'), message='已经点赞')
        ]

class LikeSerializerNew(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    author_id=serializers.SerializerMethodField(label='当前id')
    class Meta:
        model = Like
        fields = ('author','post','pub_date','id','author_id')  #若添加删除功能fields需包含“id"字段
        validators = [
            UniqueTogetherValidator(queryset=Like.objects.all(), fields=('author', 'post'), message='已经点赞')
        ]

    def get_author_id(self, obj):
        ID=obj.author.id;
        return ID