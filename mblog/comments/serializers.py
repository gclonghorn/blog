from rest_framework import serializers
from.models import Comment,Like


#序列化被回复评论信息
class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ("id", "author")  #若添加删除功能fields需包含“id"字段

#用于增删评论
class CommentSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    #reply_comment = ReplyCommentSerializer()

    class Meta:
        model = Comment
        fields = ('id','author','post','body','pub_date','reply_comment',)  #若添加删除功能fields需包含“id"字段

#用于博文详情页展示评论详情
class CommentDetailSerializer(serializers.ModelSerializer):

    reply_comment = ReplyCommentSerializer()

    class Meta:
        model = Comment
        fields = ('id','author','post','body','pub_date','reply_comment','replies')

#用于博文详情页展示点赞者列表
class LikeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('author',)

#用于增删点赞
class LikeSerializer(serializers.ModelSerializer):
    author=serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Like
        fields = ('author','post','pub_date')  #若添加删除功能fields需包含“id"字段