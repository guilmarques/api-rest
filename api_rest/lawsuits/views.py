from django.shortcuts import render
from lawsuits.models import Lawsuit
from lawsuits.serializers import LawsuitSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from lawsuits.permissions import IsOwnerOrReadOnly


class LawsuitList(generics.ListCreateAPIView):
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LawsuitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer