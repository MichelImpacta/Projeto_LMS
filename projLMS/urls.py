
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
    path('disciplina_bd/', disciplina_bd)
    path('disciplina_ads/', disciplina_ads)
    path('disciplina_adm/', disciplina_adm)
    path('disciplina_gestaoti/', disciplina_gestaoti)
    path('disciplina_jogo/', disciplina_jogo)
    path('disciplina_producao_multimidia/', disciplina_producao_multimidia)
    path('disciplina_redes/', disciplina_redes)
    path('disciplina_si/', disciplina_si)
    path('disciplina_sociedade_sustentabilidade/', disciplina_sociedade_sustentabilidade)
]

