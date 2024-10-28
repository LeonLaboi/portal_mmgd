from django.contrib import admin
from galeria.models import Perfil

class ListandoPerfis(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

# Certifique-se de que isso só apareça uma vez
admin.site.register(Perfil, ListandoPerfis)
