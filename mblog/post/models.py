from django.db import models
from django.utils import timezone
from user.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class PostCategory(models.Model):
    name=models.CharField(default="abc", max_length=200, verbose_name="类别名", help_text="类别名")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    def _unicode_(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200, default='default title',verbose_name="文章标题",help_text="博文标题")
    body=RichTextUploadingField(verbose_name="文章内容",help_text="文章内容",default='')
    pub_date=models.DateTimeField(default=timezone.now, verbose_name="发表时间",help_text="发表时间")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=1, verbose_name="作者",help_text="作者")
    category=models.ForeignKey(PostCategory, on_delete=models.CASCADE, default=1, related_name='posts',verbose_name="类别",help_text="类别")
    like_num = models.IntegerField(default=0,verbose_name="点赞数",help_text="点赞数")
    read_num = models.IntegerField(default=0, verbose_name="阅读量", help_text="阅读量")
    image= models.ImageField(upload_to='upload',null=True,blank=True,help_text='上传图片')
    file= models.FileField(upload_to='upload',null=True,blank=True,help_text='上传文件')
    excerpt=models.CharField(max_length=200,blank=True,null=True,verbose_name="文章缩略",help_text='文章简介')


    def save(self, *args, **kwargs):
        if(self.excerpt==''):
            self.excerpt=self.body[:30]
        super(Post,self).save(*args, **kwargs)



    class Meta:
        ordering=('-pub_date',)

    def _unicode_(self):
        return self.title
