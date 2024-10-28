from datetime import datetime
from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=75, null=False, blank=False)  # Corrigido max_length
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=50, null=False, blank=False)
    data_criacao = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return f'Perfil [nome={self.nome}]'

class Consumidor(models.Model):
    first_name = models.CharField(max_length=30)
    id_uc = models.IntegerField(null=False, blank=False, primary_key=True)
    id_client = models.IntegerField(null=False, blank=False, default=None)
    endereco = models.CharField(max_length=30)
    tipo = models.CharField(max_length=5, default=None)

class Gerador(models.Model):
    first_name = models.CharField(max_length=30)
    id_uc = models.IntegerField(null=False, blank=False, primary_key=True)
    id_client = models.IntegerField(null=False, blank=False, default=None)
    endereco = models.CharField(max_length=30)
    tipo = models.CharField(max_length=5, default=None)


class LeituraCSV(models.Model):
    mes_ref = models.DateField()  # mm/yyyy (precisaremos tratar isso na importação)
    dt_vcto = models.DateField()  # yyyy-mm-dd
    id_client = models.IntegerField()
    id_uc = models.IntegerField()
    grandezas = models.CharField(max_length=100)
    leitura_anterior = models.FloatField(null=True, blank=True)
    leitura_atual = models.FloatField(null=True, blank=True)
    const_medidor = models.FloatField(null=True, blank=True)
    consumo_kwh = models.FloatField(null=True, blank=True)
    qtd_enrg_tusd = models.FloatField()
    prc_unit_tributos_tusd = models.FloatField()
    tusd = models.FloatField()
    pis_cofins_tusd = models.FloatField()
    aliq_icms_tusd = models.FloatField()
    icms_tusd = models.FloatField()
    tarifa_unit_tusd = models.FloatField()
    qtd_enrg_te = models.FloatField()
    prc_unit_tributos_te = models.FloatField()
    te = models.FloatField()
    pis_cofins_te = models.FloatField()
    aliq_icms_te = models.FloatField()
    icms_te = models.FloatField()
    tarifa_unit_te = models.FloatField()
    qtd_enrg_compensada_tusd = models.FloatField(null=True, blank=True)
    prc_unit_tributos_compensada_tusd = models.FloatField(null=True, blank=True)
    compensada_tusd = models.FloatField(null=True, blank=True)
    pis_cofins_compensada_tusd = models.FloatField(null=True, blank=True)
    aliq_icms_compensada_tusd = models.FloatField(null=True, blank=True)
    icms_compensada_tusd = models.FloatField(null=True, blank=True)
    tarifa_unit_compensada_tusd = models.FloatField(null=True, blank=True)
    qtd_enrg_compensada_te = models.FloatField(null=True, blank=True)
    prc_unit_tributos_compensada_te = models.FloatField(null=True, blank=True)
    compensada_te = models.FloatField(null=True, blank=True)
    pis_cofins_compensada_te = models.FloatField(null=True, blank=True)
    aliq_icms_compensada_te = models.FloatField(null=True, blank=True)
    icms_compensada_te = models.FloatField(null=True, blank=True)
    tarifa_unit_compensada_te = models.FloatField(null=True, blank=True)
    multa = models.FloatField(null=True, blank=True)
    juros_mora = models.FloatField(null=True, blank=True)
    tx_2_emss_fat = models.FloatField(null=True, blank=True)
    dmic = models.FloatField(null=True, blank=True)
    pc_art113_ren414 = models.FloatField(null=True, blank=True)
    cosip_cip = models.FloatField()
    atualz_monetaria = models.FloatField(null=True, blank=True)
    rev_fat_atualiz = models.FloatField(null=True, blank=True)
    ren_1000 = models.FloatField(null=True, blank=True)
    art_323 = models.FloatField(null=True, blank=True)
    devol_pgto_fat_cancel = models.FloatField(null=True, blank=True)
    sem_corresp_saldo = models.FloatField(null=True, blank=True)
    cred_solu_rclm = models.FloatField(null=True, blank=True)
    cred_prox_fat = models.FloatField(null=True, blank=True)
    total = models.FloatField()
    pis_cofins_total = models.FloatField()
    icms_total = models.FloatField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"Leitura {self.id_cliente} - {self.mes_ref}"

