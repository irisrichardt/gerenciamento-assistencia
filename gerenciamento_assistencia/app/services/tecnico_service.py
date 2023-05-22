from ..models import Tecnico

def cadastrar_tecnico(tecnico):
    Tecnico.objects.create(nome=tecnico.nome, email=tecnico.email, endereco=tecnico.endereco,
                           cpf=tecnico.cpf, data_nascimento=tecnico.data_nascimento, profissao=tecnico.profissao)

def listar_tecnicos():
    return Tecnico.objects.all()

def listar_tecnico_id(id):
    return Tecnico.objects.get(id=id)

def editar_tecnico(tecnico, tecnico_novo):
    tecnico.nome= tecnico_novo.nome
    tecnico.email= tecnico_novo.email
    tecnico.endereco= tecnico_novo.endereco
    tecnico.cpf= tecnico_novo.cpf
    tecnico.data_nascimento= tecnico_novo.data_nascimento
    tecnico.profissao= tecnico_novo.profissao
    tecnico.save(force_update=True)
