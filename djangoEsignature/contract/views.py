from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# from .serializers import 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed

from drf_spectacular.utils import extend_schema


class ContractCreate(APIView):
    # @extend_schema(
    #     request=UserRegisterSerializer,
    #     responses=UserRegisterSerializer,
    # )
    # def post(self, request):
    #     ser_data = UserRegisterSerializer(data=request.POST)
    #     if ser_data.is_valid():
    #         User.objects.create_user(
    #             username=ser_data.validated_data['username'],
    #             password=ser_data.validated_data['password'],
    #         )
    #         return Response(ser_data.data, status=status.HTTP_201_CREATED)
    #     return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    pass