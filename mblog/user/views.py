
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import  get_user_model
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, mixins, viewsets, authentication, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
# from users.models import UserProfile, UserSerializer
from django.shortcuts import render,redirect
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly

# class RegList(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = RegSerializers
#     def create(self, request, *args, **kwargs):
#         res = RegSerializers(data=request.data)
#         if res.is_valid():
#             res.save()
#             # token = Token.objects.create(res)
#             # print(token.key)
#         #res.errors 定义好的错误信息
#         return Response(res.errors)

# class LogList(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = LogSerializers
#     def create(self, request, *args, **kwargs):
#         data = request.data
#         res = LogSerializers(data=data)
#         if res.is_valid():
#             return Response(res.validated_data)
#             #res.errors 定义好的错误信息
#         return Response(res.errors)

#User=get_user_model()

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserViewset(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = RegSerializers
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)#authentication.SessionAuthentication
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ('id',)

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        elif self.action=='partial_update':
            return UserUpdateSerializer
        elif self.action == "create":
            return RegSerializers
        elif self.action == "list":
            return OtherUserDetailSerializer
        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()

class UserFavViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    create:
    用户关注操作
    destroy:
    取消关注
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFvaSerializers
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly) #登录用户才有权限 ,owner才有权限删除和查看关注者
    authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)#authentication.SessionAuthentication

    def get_queryset(self):
        self.queryset= UserFav.objects.filter(user=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        instance=serializer.save()
        user = instance.user
        user.subscriber+= 1
        goods=instance.goods
        goods.follower+=1
        user.save()
        goods.save()

    def perform_destroy(self, instance):
        goods = instance.goods
        goods.follower -= 1
        goods.save()
        user = instance.user
        user.subscriber -= 1
        user.save()
        instance.delete()
