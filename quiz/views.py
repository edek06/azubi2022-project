from django.shortcuts import render, get_object_or_404
from .models import Quiz
from random import shuffle

def home(request):
    return render(request, 'quiz/home.html')

def lock(request):
    return render(request, 'quiz/lock.html')

def red(request):
    pos = Quiz.objects.get(pk=1)
    return render(request, 'quiz/red.html', {'pos':pos})

def red2(request, antwort):
    antworten = []
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=2)
    return render(request, 'quiz/red2.html', {'pos':pos, 'antworten':antworten})

def red3(request, liste, antwort):
    antworten = []
    temp_liste = len(liste)
    antworten.append(liste[2:temp_liste - 2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=3)
    return render(request, 'quiz/red3.html', {'pos':pos, 'antworten':antworten})

def red4(request, liste, antwort):
    antworten = []
    antwort1, antwort2 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=4)
    return render(request, 'quiz/red4.html', {'pos':pos, 'antworten':antworten})

def summary(request, liste, antwort):
    antworten = []
    antworten_richtig = []
    summary = {}

    antwort1, antwort2, antwort3 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-1])
    antworten.append(antwort3[2:len(antwort3)-2])
    antworten.append(antwort)

    pos1 = Quiz.objects.get(pk=1)
    antworten_richtig.append(pos1.richtig)
    pos2 = Quiz.objects.get(pk=2)
    antworten_richtig.append(pos2.richtig)
    pos3 = Quiz.objects.get(pk=3)
    antworten_richtig.append(pos3.richtig)
    pos4 = Quiz.objects.get(pk=4)
    antworten_richtig.append(pos4.richtig)

    for i in range(4):
        if antworten[i] == antworten_richtig[i]:
            summary[antworten[i]] = "Richtig"
        else:
            summary[antworten[i]] = "Falsch"

    return render(request, 'quiz/summary.html', {'antworten':antworten, 'summary':summary})

def green(request):
    pos = Quiz.objects.get(pk=5)
    return render(request, 'quiz/green.html', {'pos':pos})

def green2(request, antwort):
    antworten = []
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=6)
    return render(request, 'quiz/green2.html', {'pos':pos, 'antworten':antworten})

def green3(request, liste, antwort):
    antworten = []
    temp_liste = len(liste)
    antworten.append(liste[2:temp_liste - 2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=7)
    return render(request, 'quiz/green3.html', {'pos':pos, 'antworten':antworten})

def green4(request, liste, antwort):
    antworten = []
    antwort1, antwort2 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=8)
    return render(request, 'quiz/green4.html', {'pos':pos, 'antworten':antworten})

def summary2(request, liste, antwort):
    antworten = []
    antworten_richtig = []
    summary = {}

    antwort1, antwort2, antwort3 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-1])
    antworten.append(antwort3[2:len(antwort3)-2])
    antworten.append(antwort)

    pos1 = Quiz.objects.get(pk=5)
    antworten_richtig.append(pos1.richtig)
    pos2 = Quiz.objects.get(pk=6)
    antworten_richtig.append(pos2.richtig)
    pos3 = Quiz.objects.get(pk=7)
    antworten_richtig.append(pos3.richtig)
    pos4 = Quiz.objects.get(pk=8)
    antworten_richtig.append(pos4.richtig)

    for i in range(4):
        if antworten[i] == antworten_richtig[i]:
            summary[antworten[i]] = "Richtig"
        else:
            summary[antworten[i]] = "Falsch"

    return render(request, 'quiz/summary2.html', {'antworten':antworten, 'summary':summary})

def black(request):
    liste = list(range(9,18))
    shuffle(liste)
    pos = Quiz.objects.get(pk=liste[0])
    return render(request, 'quiz/black.html', {'pos':pos})

def black2(request, antwort):
    antworten = []
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=10)
    return render(request, 'quiz/black2.html', {'pos':pos, 'antworten':antworten})

def black3(request, liste, antwort):
    antworten = []
    temp_liste = len(liste)
    antworten.append(liste[2:temp_liste - 2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=11)
    return render(request, 'quiz/black3.html', {'pos':pos, 'antworten':antworten})

def black4(request, liste, antwort):
    antworten = []
    antwort1, antwort2 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=12)
    return render(request, 'quiz/black4.html', {'pos':pos, 'antworten':antworten})

def black5(request, liste, antwort):
    antworten = []
    antwort1, antwort2, antwort3 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-1])
    antworten.append(antwort3[2:len(antwort3)-2])
    antworten.append(antwort)
    pos = Quiz.objects.get(pk=13)
    return render(request, 'quiz/black5.html', {'pos':pos, 'antworten':antworten})

def summary3(request, antwort, richtig):
    answer = antwort
    summary = {}

    if antwort == richtig:
        summary[answer] = "Richtig"
    else:
        summary[answer] = "Falsch"

    return render(request, 'quiz/summary3.html', {'summary': summary})
"""
    antwort1, antwort2, antwort3, antwort4 = liste.split(',')
    antworten.append(antwort1[2:len(antwort1)-1])
    antworten.append(antwort2[2:len(antwort2)-1])
    antworten.append(antwort3[2:len(antwort3)-1])
    antworten.append(antwort4[2:len(antwort4)-2])
    antworten.append(antwort)

    pos1 = Quiz.objects.get(pk=9)
    antworten_richtig.append(pos1.richtig)
    pos2 = Quiz.objects.get(pk=10)
    antworten_richtig.append(pos2.richtig)
    pos3 = Quiz.objects.get(pk=11)
    antworten_richtig.append(pos3.richtig)
    pos4 = Quiz.objects.get(pk=12)
    antworten_richtig.append(pos4.richtig)
    pos5 = Quiz.objects.get(pk=13)
    antworten_richtig.append(pos5.richtig)

    for i in range(5):
        if antworten[i] == antworten_richtig[i]:
            summary[antworten[i]] = "Richtig"
        else:
            summary[antworten[i]] = "Falsch"
"""

