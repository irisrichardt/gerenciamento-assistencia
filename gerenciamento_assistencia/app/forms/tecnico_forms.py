from django import forms
from django.forms import DateInput

from ..models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            )
        }
