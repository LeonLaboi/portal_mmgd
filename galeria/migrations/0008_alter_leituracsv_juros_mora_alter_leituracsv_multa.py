# Generated by Django 4.2.16 on 2024-10-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_leituracsv_art_323_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leituracsv',
            name='juros_mora',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leituracsv',
            name='multa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
