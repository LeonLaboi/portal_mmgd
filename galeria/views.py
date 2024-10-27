import json
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

from django.shortcuts import render, get_object_or_404 #get_list_or_404
from django.http import JsonResponse #HttpResponse
from django.templatetags.static import static

from galeria.models import Perfil, LeituraCSV


def index(request):
  
    image_path = "https://static.wixstatic.com/media/f98783_421f8b496bf44a31a146dd289460e2ae~mv2_d_4000_2000_s_2.jpg/v1/fill/w_1903,h_811,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/f98783_421f8b496bf44a31a146dd289460e2ae~mv2_d_4000_2000_s_2.jpg"
    context = {
        'image_path': image_path,
        'welcome_message': "CONVIDAMOS COOPERATIVAS \
                           A REPENSAREM SEUS MODOS DE GERAÇÃO E CONSUMO DE ENERGIA!"
    }
    return render(request, 'galeria/index.html', context)#return render(request, 'index.html') #


def alura(request):
    perfis = Perfil.objects.all()
    return render(request, 'galeria/alura.html', {'cards': perfis})


def imagem(request, perfil_id):
    perfil = get_object_or_404(Perfil, pk=perfil_id)

    if perfil.nome == 'Gestor de Energia':
        clientes = LeituraCSV.objects.values('id_client').distinct()
        selected_filter = 'id_client'
    else:
        clientes = LeituraCSV.objects.values('id_uc').distinct()
        selected_filter = 'id_uc'

    selected_id = request.GET.get(selected_filter, clientes[0][selected_filter])
    leituras = LeituraCSV.objects.filter(**{selected_filter: selected_id})

    mes_refs = [leitura.mes_ref.strftime("%m/%Y") for leitura in leituras]
    qtd_enrg_te = [leitura.qtd_enrg_te for leitura in leituras]

    plt.figure(figsize=(10, 5))
    plt.bar(mes_refs, qtd_enrg_te, color='skyblue')
    plt.title(f'Quantidade de Energia por Mês para {selected_filter}={selected_id}')
    plt.xlabel('Mês Referência')
    plt.ylabel('Quantidade de Energia (kWh)')
    plt.xticks(rotation=45)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'galeria/imagem.html', {
        'perfil': perfil,
        'graphic': graphic,
        'clientes': clientes,
        'selected_filter': selected_filter,
        'selected_id': selected_id,
    })


def get_graph(request, client_id):
    # Obtém os dados do gráfico para o cliente específico
    leituras = LeituraCSV.objects.filter(id_client=client_id).values('mes_ref', 'qtd_enrg_te')

    # Criação do gráfico
    meses = [leitura['mes_ref'] for leitura in leituras]
    consumos = [leitura['qtd_enrg_te'] for leitura in leituras]

    plt.figure(figsize=(10, 5))
    plt.bar(meses, consumos)
    plt.xlabel('Meses')
    plt.ylabel('Quantidade de Energia (kWh)')
    plt.title(f'Consumo de Energia para Cliente ID {client_id}')

    # Salvar o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    
    # Codificar o gráfico em base64
    graphic = base64.b64encode(buf.read()).decode('utf-8')
    return JsonResponse({'graphic': graphic})

# def imagem(request, perfil_id):
#     perfil = get_list_or_404(Perfil, pk=perfil_id) #Perfil.objects.get(id=foto_id)
#     return render(request, 'galeria/imagem.html', {'perfil': perfil})

# def imagem_view(request):
#     id_cliente = request.GET.get('id_cliente', None)
#     if id_cliente:
#         dados = LeituraCSV.objects.filter(id_cliente=id_cliente).values('mes_ref', 'qtd_enrg_te')
#     else:
#         dados = LeituraCSV.objects.all().values('mes_ref', 'qtd_enrg_te', 'id_cliente')

#     # Converte os dados para JSON
#     dados_json = json.dumps(list(dados))

#     # Busca todos os IDs únicos de cliente para o campo de seleção
#     ids_clientes = LeituraCSV.objects.values_list('id_cliente', flat=True).distinct()

#     return render(request, 'galeria/imagem.html', {
#         'dados': dados_json,
#         'ids_clientes': ids_clientes,
#     })