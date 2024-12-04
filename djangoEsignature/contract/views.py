from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Contract, EmailContract
from .serializers import MessageEmailsSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from rest_framework.exceptions import AuthenticationFailed

from drf_spectacular.utils import extend_schema


class ContractCreate(APIView):
    authentication_classes = [IsAuthenticated,]
    @extend_schema(
        request=MessageEmailsSerializer,
        responses=MessageEmailsSerializer,
    )
    def post(self, request):
        ser_data = MessageEmailsSerializer(data=request.POST)
        if ser_data.is_valid():
            Contract.objects.create(text=ser_data.validated_data['text'], user=request.User)
        
        

            
    #         return Response(ser_data.data, status=status.HTTP_201_CREATED)
    #     return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)