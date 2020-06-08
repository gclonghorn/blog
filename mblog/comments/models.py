from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from post.models import Post
# Create your models here.

User=get_user_model()

class Comment (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='comments',  verbose_name="作者")
    post=models.ForeignKey(Post, on_delete=models.CASCADE, default=1, related_name='comments', verbose_name="文章", help_text="被评论文章")
    body = models.TextField(verbose_name="评论内容", help_text="评论内容")
    pub_date=models.DateTimeField(default=timezone.now, verbose_name="发表时间", help_text="发表时间")
    reply_comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True,help_text="父级评论")
    #related_name 便于主表查子表即评论有哪些回复 .reply_comment说明这条评论属于哪个

    class Meta:
        ordering=('-pub_date',)

    def _unicode_(self):
        return self.body



class Like (models.Model):
    """
    用户点赞
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,related_name='likes', verbose_name="点赞者")
    post=models.ForeignKey(Post, on_delete=models.CASCADE, default=1,related_name='likes', verbose_name="文章",help_text="被赞文章")
    pub_date=models.DateTimeField(default=timezone.now, verbose_name="发表时间",help_text="点赞时间")


    class Meta:
        ordering=('-pub_date',)
        unique_together = ("author", "post")  #一个用户对一个文章只能点赞一次

    def _unicode_(self):
        return self.author.username