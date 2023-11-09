from django.shortcuts import render
from . import matematica_gamer as mg
from django.http import JsonResponse

# Create your views here.

def index(request):
    requisicao = mg.generate_question()
    
    return render(request, 'index.html', {'requisicao': requisicao})

def iniciarJogo(request):
    requisicao = mg.generate_question()
    return JsonResponse({'resposta': requisicao})
