# -*- coding: utf-8 -*-
from rest_framework import serializers
from lawsuits.models import Lawsuit
from lawsuits.utils import is_number
from django.contrib.auth.models import User


class LawsuitSerializer(serializers.ModelSerializer):
    number = serializers.CharField(min_length=20, max_length=20, validators=[is_number])
    #user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Lawsuit
        fields = ('id', 'data', 'number', 'user')


class UserSerializer(serializers.ModelSerializer):
    lawsuits = serializers.PrimaryKeyRelatedField(many=True, queryset=Lawsuit.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'lawsuits')