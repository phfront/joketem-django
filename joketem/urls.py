from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from joketem.joketemapp import views

urlpatterns = [
    path('api/joke', views.JokeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)