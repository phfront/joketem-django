# from django.urls import include, path
# from rest_framework import routers
# from joketem.joketemapp import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# # router.register(r'joke', views.JokeViewSet)
# router.register(r'joke', views.RandomJokeView.as_view())

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('joke', views.RandomJokeView.as_view()),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .joketemapp import views

urlpatterns = [
    path('api/joke/', views.RandomJokeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)