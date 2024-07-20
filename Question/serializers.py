from rest_framework.serializers import ModelSerializer

from .models import User


class User_Serializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Certificate_Serializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['correct_answer', 'wrong_answer', 'score']
