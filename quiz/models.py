from django.db import models

class Quiz(models.Model):
    frage = models.CharField(max_length=200)
    antwort1 = models.CharField(max_length=50)
    antwort2 = models.CharField(max_length=50)
    antwort3 = models.CharField(max_length=50)
    antwort4 = models.CharField(max_length=50)