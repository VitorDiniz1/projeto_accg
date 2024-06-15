from django.db import models

# Create your models here.
from django.db import models
class Animais(models.Model):
    sexo = {
        "F": "Fêmea",
        "M": "Macho",
    }
    tipo = {
        "Gato": "Gato",
        "Cachorro": "Cachorro",
    }
    porte = {
        "Pequeno Porte": "Pequeno Porte",
        "Médio Porte": "Médio Porte",
        "Grande Porte": "Grande Porte",
    }
    idade = {
        "Filhote": "Filhote",
        "Adulto": "Adulto",
        "Idoso": "Idoso",
    }
    nome = models.CharField(max_length=30)
    idade = models.CharField(max_length=10, choices=idade)
    descricao = models.TextField()
    castrado = models.BooleanField()
    vacinado = models.BooleanField()
    vermifugado = models.BooleanField()
    fiv = models.BooleanField(default=False)
    felv = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=sexo)
    tipo = models.CharField(max_length=10, choices=tipo)
    porte = models.CharField(max_length=20, choices=porte, default=porte["Médio Porte"])
    url_imagem = models.CharField(max_length=100, default="https://static.wixstatic.com/media/f94f12_6af5c43bf13048b9b0d22534c7ed9cd7~mv2.png")

