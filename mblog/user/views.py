import uuid

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, mixins, viewsets, authentication, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
# from users.models import UserProfile, UserSerializer
from django.shortcuts import render,redirect
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token

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



class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(tel=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = RegSerializers
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return RegSerializers
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