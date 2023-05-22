from ..models import Tecnico

def cadastrar_tecnico(tecnico):
    Tecnico.objects.create(nome=tecnico.nome, email=tecnico.email, endereco=tecnico.endereco,
                           cpf=tecnico.cpf, data_nascimento=tecnico.data_nascimento, profissao=tecnico.profissao)

def listar_tecnicos():
    return Tecnico.objects.all()

def listar_tecnico_id(id):
    return Tecnico.objects.get(id=id)
