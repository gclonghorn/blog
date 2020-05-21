from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    """
    用户
    """

    username = models.CharField(max_length=200, default='abc', unique=True,verbose_name="用户名")
    #password = models.CharField(max_length=200, default='0', unique=True,verbose_name="密码")
    password = models.CharField(max_length=256, null=True, blank=True, verbose_name="密码")
    tel = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="邮箱")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="注册时间")
    introduction = models.CharField(max_length=300, null=True, blank=True, verbose_name="个人简介")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
