from django.urls import path
from .views import index, alura  # Importando as views necessárias

urlpatterns = [
    path('', index, name='index') , #Página inicial
    path('alura/', alura, name='alura')#, Página alura
]
