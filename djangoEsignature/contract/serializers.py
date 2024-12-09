from rest_framework import serializers
from .models import UsersInfo

class UsersInfoSerializer(serializers.ModelSerializer):

    class Meta :
        model = UsersInfo
        fields = ('fullname', 'email',)
    