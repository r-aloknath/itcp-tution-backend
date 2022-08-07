from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    slNo=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    mobile=serializers.IntegerField()
    position=serializers.CharField(max_length=100)
    remarks=serializers.CharField(max_length=400)
    eMail=serializers.CharField(max_length=50)

