from django.forms import ModelForm
from app.models import Animais

# Create the form class.
class AnimaisForm(ModelForm):
    class Meta:
        model = Animais
        fields = ["nome", "idade", "descricao", "castrado", "vacinado", "vermifugado", "fiv", "felv", "sexo", "tipo", "url_imagem", "porte"]
