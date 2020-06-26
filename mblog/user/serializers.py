from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from user.models import User,UserFav
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import raise_errors_on_nested_writes,model_meta

#注册
class RegSerializers(serializers.ModelSerializer):
    pwd2 = serializers.CharField(max_length=256, min_length=4, write_only=True)
    tel = serializers.CharField(max_length=11, min_length=11)
    class Meta:
        model = User
        fields=('username', 'password', 'pwd2', 'tel', 'email', 'introduction')
    def validate(self, attrs):
        if attrs['pwd2'] != attrs['password']:
            raise ValidationError('两次密码输入不一致')
        del attrs['pwd2']
 		#对密码进行加密 make_password
        attrs['password'] = make_password(attrs['password'])
        return attrs


# #登录
# class LogSerializers(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=6)
#     class Meta:
#         model = UserProfile
#         fields = ('username', 'password')
#     def validate(self, attrs):
#         user_obj=UserProfile.objects.filter(username=attrs['username']).first()
#         if user_obj:
#         #check_password　可以将加密后的密码与输入的密码进行对比
#             if check_password(attrs['password'], user_obj.password):
#                 return attrs
#         raise ValidationError('用户名或密码错误')



from browse.serializers import PostDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from datetime import datetime
from datetime import timedelta
import re
User = get_user_model()


#用于粉丝概要信息
class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id",'head')
#用于粉丝概要信息
class UserSrializer3(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",)

class followSerializer(serializers.ModelSerializer):
    user=UserSrializer()
    class Meta:
        model=UserFav
        fields=('user','id')
class OtherUserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    posts = PostDetailSerializer(many=True)
    class Meta:
        model = User
        fields = ("username", "tel", "email", "introduction", 'id','reg_date','posts','follower','subscriber','head')#'posts'
        #ids关注者 usernames粉丝
class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    posts = PostDetailSerializer(many=True)
    class Meta:
        model = User
        fields = ("username", "tel", "email", "introduction", 'password','id','reg_date','posts','follower','subscriber','head')#'posts'
        #ids关注者 usernames粉丝
class UserUpdateSerializer(serializers.ModelSerializer):
    """
    用户修改信息序列化类
    """
   # posts = PostDetailSerializer(many=True)
    #usernames = followSerializer(many=True, read_only=True)  # 粉丝
   # ids = followSerializer(many=True, read_only=True)  # 关注者
    class Meta:
        model = User
        fields = ("username", "tel", "email", "introduction", 'password','id','reg_date','head')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.email = validated_data.get('email', instance.email)
        instance.head = validated_data.get('head', instance.head)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance



class UserFvaSerializers(serializers.ModelSerializer):
    """
    用户关注
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # validate实现唯一联合，一个人只能关注一次
    validators = [
        UniqueTogetherValidator(queryset=UserFav.objects.all(), fields=('user', 'goods'), message='已经关注')
    ]

    class Meta:
        model = UserFav
        fields = ['user', 'goods', 'id'] #goods关注者 usernames粉丝



# class UserRegSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
#                                      validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
#
#     password = serializers.CharField(
#         style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,
#     )
#
#     # def create(self, validated_data):
#     #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
#     #     user.set_password(validated_data["password"])
#     #     user.save()
#     #     return user
#
#     def validate(self, attrs):
#         attrs["tel"] = attrs["username"]
#         del attrs["code"]
#         return attrs
#
#     class Meta:
#         model = User
#         fields = ("username", "tel", "password")
