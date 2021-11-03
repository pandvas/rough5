from django.db.models import fields
from rest_framework import serializers
from .models import Jobregistration,Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class jobregistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Jobregistration
        fields = '__all__'
        

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields= '__all__'


