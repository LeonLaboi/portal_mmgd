from django.urls import path
from .views import index, alura, imagem  # Importando as views necessárias

urlpatterns = [
    path('', index, name='index'), #Página inicial
    path('alura/', alura, name='alura'), #Página alura
    path('imagem/<int:perfil_id>', imagem, name='imagem'),
]
