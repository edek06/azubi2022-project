from django.db import models

class Quiz(models.Model):
    kategorie = models.CharField(max_length=50)
    frage = models.CharField(max_length=200)
    antwort1 = models.CharField(max_length=100)
    antwort2 = models.CharField(max_length=100)
    antwort3 = models.CharField(max_length=100)
    antwort4 = models.CharField(max_length=100)
    richtig = models.CharField(max_length=100)