from django.shortcuts import render, get_object_or_404
from .models import Quiz

def home(request):
    return render(request, 'quiz/home.html')

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

def schwarzfehler1(request):
    return render(request, 'quiz/schwarzfehler1.html')

def schwarzfehler2(request):
    return render(request, 'quiz/schwarzfehler2.html')

def schwarzfehler3(request):
    return render(request, 'quiz/schwarzfehler3.html')

def schwarz2(request):
    return render(request, 'quiz/schwarz2.html')

def schwarz2fehler1(request):
    return render(request, 'quiz/schwarz2fehler1.html')

def schwarz2fehler2(request):
    return render(request, 'quiz/schwarz2fehler2.html')

def schwarz2fehler3(request):
    return render(request, 'quiz/schwarz2fehler3.html')

def schwarz3(request):
    return render(request, 'quiz/schwarz3.html')

def schwarz3fehler1(request):
    return render(request, 'quiz/schwarz3fehler1.html')

def schwarz3fehler2(request):
    return render(request, 'quiz/schwarz3fehler2.html')

def schwarz3fehler3(request):
    return render(request, 'quiz/schwarz3fehler3.html')

def schwarz4(request):
    return render(request, 'quiz/schwarz4.html')

def schwarz4fehler1(request):
    return render(request, 'quiz/schwarz4fehler1.html')

def schwarz4fehler2(request):
    return render(request, 'quiz/schwarz4fehler2.html')

def schwarz4fehler3(request):
    return render(request, 'quiz/schwarz4fehler3.html')

def schwarz5(request):
    return render(request, 'quiz/schwarz5.html')

def schwarz5fehler1(request):
    return render(request, 'quiz/schwarz5fehler1.html')

def schwarz5fehler2(request):
    return render(request, 'quiz/schwarz5fehler2.html')

def schwarz5fehler3(request):
    return render(request, 'quiz/schwarz5fehler3.html')

def gruen(request):
    return render(request, 'quiz/gruen.html')

def gruenfehler1(request):
    return render(request, 'quiz/gruenfehler1.html')

def gruenfehler2(request):
    return render(request, 'quiz/gruenfehler2.html')

def gruenfehler3(request):
    return render(request, 'quiz/gruenfehler3.html')

def gruen2(request):
    return render(request, 'quiz/gruen2.html')

def gruen2fehler1(request):
    return render(request, 'quiz/gruen2fehler1.html')

def gruen2fehler2(request):
    return render(request, 'quiz/gruen2fehler2.html')

def gruen2fehler3(request):
    return render(request, 'quiz/gruen2fehler3.html')

def gruen3(request):
    return render(request, 'quiz/gruen3.html')

def gruen3fehler1(request):
    return render(request, 'quiz/gruen3fehler1.html')

def gruen3fehler2(request):
    return render(request, 'quiz/gruen3fehler2.html')

def gruen3fehler3(request):
    return render(request, 'quiz/gruen3fehler3.html')

def gruen4(request):
    return render(request, 'quiz/gruen4.html')

def gruen4fehler1(request):
    return render(request, 'quiz/gruen4fehler1.html')

def gruen4fehler2(request):
    return render(request, 'quiz/gruen4fehler2.html')

def gruen4fehler3(request):
    return render(request, 'quiz/gruen4fehler3.html')

def rotfehler1(request):
    return render(request, 'quiz/rotfehler1.html')

def rotfehler2(request):
    return render(request, 'quiz/rotfehler2.html')

def rotfehler3(request):
    return render(request, 'quiz/rotfehler3.html')

def rot2fehler1(request):
    return render(request, 'quiz/rot2fehler1.html')

def rot2fehler2(request):
    return render(request, 'quiz/rot2fehler2.html')

def rot2fehler3(request):
    return render(request, 'quiz/rot2fehler3.html')

def rot3fehler1(request):
    return render(request, 'quiz/rot3fehler1.html')

def rot3fehler2(request):
    return render(request, 'quiz/rot3fehler2.html')

def rot3fehler3(request):
    return render(request, 'quiz/rot3fehler3.html')

def rot4fehler1(request):
    return render(request, 'quiz/rot4fehler1.html')

def rot4fehler2(request):
    return render(request, 'quiz/rot4fehler2.html')

def rot4fehler3(request):
    return render(request, 'quiz/rot4fehler3.html')