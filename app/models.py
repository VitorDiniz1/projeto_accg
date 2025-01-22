from django.db import models

class Animais(models.Model):
    SEXO_CHOICES = [
        ("F", "Fêmea"),
        ("M", "Macho"),
    ]
    TIPO_CHOICES = [
        ("Gato", "Gato"),
        ("Cachorro", "Cachorro"),
    ]
    PORTE_CHOICES = [
        ("Pequeno Porte", "Pequeno Porte"),
        ("Médio Porte", "Médio Porte"),
        ("Grande Porte", "Grande Porte"),
    ]
    IDADE_CHOICES = [
        ("Filhote", "Filhote"),
        ("Adulto", "Adulto"),
        ("Idoso", "Idoso"),
    ]

    nome = models.CharField(max_length=30)
    idade = models.CharField(max_length=10, choices=IDADE_CHOICES)
    descricao = models.TextField()
    castrado = models.BooleanField()
    vacinado = models.BooleanField()
    vermifugado = models.BooleanField()
    fiv = models.BooleanField(default=False)
    felv = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    porte = models.CharField(max_length=20, choices=PORTE_CHOICES, default="Médio Porte")
    url_imagem = models.CharField(
        max_length=255,
        default="https://static.wixstatic.com/media/f94f12_6af5c43bf13048b9b0d22534c7ed9cd7~mv2.png"
    )

    def __str__(self):
        return f"{self.nome} - {self.tipo}"
