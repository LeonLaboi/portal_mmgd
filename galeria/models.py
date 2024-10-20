from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=75, null=False, blank=False)  # Corrigido max_length
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'Perfil [nome={self.nome}]'

class Consumidor(models.Model):
    first_name = models.CharField(max_length=30)
    id_uc = models.IntegerField(null=False, blank=False, primary_key=True)
    endereco = models.CharField(max_length=30)

class Gerador(models.Model):
    first_name = models.CharField(max_length=30)
    id_uc = models.IntegerField(null=False, blank=False, primary_key=True)
    endereco = models.CharField(max_length=30)
