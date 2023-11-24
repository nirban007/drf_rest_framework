from rest_framework import serializers
from .models import Contract

# class ContractSerializer(serializers.Serializer):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]

#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     mobile = serializers.CharField(max_length=100)
#     date_of_birth = serializers.DateField()
#     gender = serializers.ChoiceField(choices=GENDER_CHOICES)

#     def create(self, validated_data):
#         return Contract.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.mobile = validated_data.get('mobile', instance.mobile)
#         instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.save()
#         return instance

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'gender']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = ['first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'gender']
