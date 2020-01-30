from django.db import models

class Joke(models.Model):
    number = models.IntegerField()
    text = models.TextField()