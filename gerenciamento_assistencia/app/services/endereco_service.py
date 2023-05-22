from ..models import EnderecoTecnico

def cadastrar_endereco(endereco):
    return EnderecoTecnico.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)
