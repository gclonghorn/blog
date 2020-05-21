from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class PostCategory(models.Model):
    name=models.CharField(default="abc", max_length=200, verbose_name="类别名", help_text="类别名")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    def _unicode_(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name="文章标题")
    slug=models.CharField(max_length=200)
    body=models.TextField(verbose_name="文章内容")
    pub_date=models.DateTimeField(default=timezone.now, verbose_name="发表时间")
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="作者")
    category=models.ForeignKey(PostCategory, on_delete=models.CASCADE, default=1, verbose_name="类别")

    class Meta:
        ordering=('-pub_date',)

    def _unicode_(self):
        return self.title
