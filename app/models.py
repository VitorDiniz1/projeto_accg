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
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    descricao = models.TextField()
    castrado = models.BooleanField()
    vacinado = models.BooleanField()
    vermifugado = models.BooleanField()
    sexo = models.CharField(max_length=1, choices=sexo)
    tipo = models.CharField(max_length=10, choices=tipo)

