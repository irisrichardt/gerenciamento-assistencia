from django import forms
from ..models import EnderecoTecnico

class EnderecoTecnicoForm(forms.ModelForm):
    class Meta:
        model = EnderecoTecnico
        fields = ['rua', 'cidade', 'estado']
