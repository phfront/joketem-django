from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from joketem.joketemapp.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from random import randint

import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class JokeList(APIView):
    """
    List all jokes
    """
    def get(self, request, format=None):
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        with open('joketem/joketemapp/jokes.json', 'r') as f:
            jokes = json.load(f)
        return Response(jokes[randint(0, len(jokes) - 1)])