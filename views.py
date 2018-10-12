from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def disciplinas(request):
    return render(request,'disciplinas.html')

def listaDeCursos(request):
    return render(request,'listaDeCursos.html')

def noticias(request):
    return render(request,'noticias.html')

def noticia1(request):
    return render(request,'noticia1.html')
