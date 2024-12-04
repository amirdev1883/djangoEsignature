from rest_framework import serializers

class MessageEmailsSerializer(serializers.Serializer):
    message = serializers.CharField(
        max_length=500, 
        allow_blank=False 
    )
    emails = serializers.ListField(
        child=serializers.EmailField(),
        allow_empty=False,  
        min_length=1,       
    )