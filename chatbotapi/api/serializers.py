from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only" : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ["id", "pattern", "intent"]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "answer", "intent"]

class IntentSerializer(serializers.ModelSerializer):
    patterns = PatternSerializer(many = True, required = False)
    answers = AnswerSerializer(many = True, required = False)
    
    class Meta:
        model = Intent
        fields = ["id", "tagname", "patterns", "answers"]
