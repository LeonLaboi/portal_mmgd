# Generated by Django 4.2.16 on 2024-10-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('legenda', models.CharField(max_length=75)),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=50)),
            ],
        ),
    ]