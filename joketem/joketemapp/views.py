from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from joketem.joketemapp.serializers import UserSerializer, GroupSerializer, JokeSerializer
from rest_framework.response import Response
from random import randint
from .models import Joke

from rest_framework.parsers import JSONParser
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

class RandomJokeView(APIView):
    """
    List all jokes
    """
    def get(self, request, format=None):
        count = Joke.objects.all().count()
        joke = Joke.objects.get(number=randint(1, count));
        serializer = JokeSerializer(joke, many=False)
        return Response(serializer.data['text'])
        # return Response(jokes[randint(0, len(jokes) - 1)])