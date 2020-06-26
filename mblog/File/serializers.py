from rest_framework import serializers
from.models import File

#用于资源上传下载
class FileSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    class Meta:
        model = File
        fields = ('file','id','author','post','name','pub_date')


