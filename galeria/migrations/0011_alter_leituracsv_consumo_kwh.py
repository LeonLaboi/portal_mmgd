# Generated by Django 4.2.16 on 2024-10-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0010_alter_leituracsv_const_medidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leituracsv',
            name='consumo_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
    ]