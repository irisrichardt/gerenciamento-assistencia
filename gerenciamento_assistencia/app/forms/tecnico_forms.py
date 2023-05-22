from django import forms
from ..models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
