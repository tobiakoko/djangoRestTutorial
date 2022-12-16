from django.contrib.auth.models import User, Group
from rest_framework import serializers

class USerSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Mets:
        model = Group
        fields = ['url', 'name']