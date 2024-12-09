from rest_framework import serializers

class ContractRecepientsSerializers(serializers.Serializer):
    text = serializers.CharField(
        max_length=500, 
        allow_blank=False 
    )
    emails = serializers.ListField(
        child=serializers.EmailField(),
        allow_empty=False,  
        min_length=1,       
    )
    fullnames = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,  
        min_length=1,       
    )