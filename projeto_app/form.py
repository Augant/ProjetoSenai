from django import forms
from .models import contato  # Importa o modelo Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = contato
        fields = ['nome', 'email', 'data_nascimento']
        # Aqui você pode adicionar outras opções, como widgets personalizados