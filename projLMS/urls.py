
from django.contrib import admin
from django.urls import path
from faculdade.views import *

urlpatterns = [
    path('',index),
    path('disciplinas/',disciplinas),
    path('listaDeCursos/',listaDeCursos),
    path('noticias/',noticias),
    path('noticia1/',noticia1),
    path('admin/', admin.site.urls),
]

