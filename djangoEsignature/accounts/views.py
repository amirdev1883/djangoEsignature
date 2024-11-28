from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed

from drf_spectacular.utils import extend_schema


class UserRegister(APIView):
    @extend_schema(
        request=UserRegisterSerializer,
        responses=UserRegisterSerializer,
    )
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username=ser_data.validated_data['username'],
                password=ser_data.validated_data['password'],
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    @extend_schema(
        request=UserLoginSerializer,
        responses=UserLoginSerializer,
    )
    def post(self, request):
        ser_data = UserLoginSerializer(data=request.POST)
        if ser_data.is_valid():
            user = authenticate(request, username=ser_data.validated_data['username'], password=ser_data.validated_data['password'])
            if not user:
                raise AuthenticationFailed('Invalid credentials')
            login(request, user)
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'message':'you logouted succesfully'})