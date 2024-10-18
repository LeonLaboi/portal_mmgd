from django.shortcuts import render
# from django.http import HttpResponse
from django.templatetags.static import static

def index(request):
  
    image_path = "https://static.wixstatic.com/media/f98783_421f8b496bf44a31a146dd289460e2ae~mv2_d_4000_2000_s_2.jpg/v1/fill/w_1903,h_811,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/f98783_421f8b496bf44a31a146dd289460e2ae~mv2_d_4000_2000_s_2.jpg"
    context = {
        'image_path': image_path,
        'welcome_message': "CONVIDAMOS COOPERATIVAS \
                           A REPENSAREM SEUS MODOS DE GERAÇÃO E CONSUMO DE ENERGIA!"
    }
    return render(request, 'galeria/index.html', context)#return render(request, 'index.html') #


def alura(request):
    return render(request, 'galeria/alura.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

