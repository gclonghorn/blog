from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    """
    用户
    """

    username = models.CharField(max_length=200, unique=True, null=True, blank=True,verbose_name="用户名")
    password = models.CharField(max_length=256, null=True, blank=True, verbose_name="密码")
    tel = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="邮箱")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="注册时间")
    introduction = models.CharField(max_length=300, null=True, blank=True, verbose_name="个人简介")
    reg_date = models.DateTimeField(default=timezone.now, verbose_name="注册时间", help_text="注册时间")
    head=models.ImageField(upload_to='upload',null=True,blank=True,verbose_name="头像",help_text="头像")
    subscriber=models.IntegerField(default=0,verbose_name="已关注数",help_text="已关注数")
    follower = models.IntegerField(default=0,verbose_name='粉丝数',help_text='粉丝数')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserFav(models.Model):
    """

    """
    user = models.ForeignKey(User, related_name="ids", on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(User, related_name="usernames", on_delete=models.CASCADE, verbose_name="商品",help_text='关注人')
    add_time = models.DateTimeField("添加时间",default=timezone.now)

    class Meta:
        verbose_name = '用户关注'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username
