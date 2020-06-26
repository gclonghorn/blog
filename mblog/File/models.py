from django.db import models
from django.utils import timezone
from user.models import User
from post.models import Post
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class File(models.Model):
    name =models.CharField(max_length=200,null=True, blank=True,)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='files',default=1, verbose_name="作者",help_text="上传人")
    post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True, default=1,related_name='files', verbose_name="文章",help_text="博文")
    file= models.FileField(upload_to='upload',null=True,blank=True,help_text='上传文件')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="发表时间", help_text="点赞时间")

    class Meta:
        ordering=('-pub_date',)

    def _unicode_(self):
        return self.author
