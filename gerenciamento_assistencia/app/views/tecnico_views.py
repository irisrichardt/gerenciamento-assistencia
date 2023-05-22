from django.shortcuts import redirect, render

from ..forms.tecnico_forms import TecnicoForm
from ..forms.endereco_forms import EnderecoTecnicoForm
from ..entidades import tecnico, endereco
from ..services import tecnico_service, endereco_service

def cadastrar_tecnico(request):
    if request.method == "POST":
        form_tecnico = TecnicoForm(request.POST)
        form_endereco = EnderecoTecnicoForm(request.POST)

        if form_tecnico.is_valid():
            nome = form_tecnico.cleaned_data["nome"]
            email = form_tecnico.cleaned_data["email"]
            cpf = form_tecnico.cleaned_data["cpf"]
            data_nascimento = form_tecnico.cleaned_data["data_nascimento"]
            profissao = form_tecnico.cleaned_data["profissao"]
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                tecnico_novo = tecnico.Tecnico(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_bd)
                tecnico_service.cadastrar_tecnico(tecnico_novo)
                return redirect('listar_tecnicos')
    else:
        form_tecnico = TecnicoForm()
        form_endereco = EnderecoTecnicoForm()
    return render(request, 'tecnicos/form_tecnico.html', {'form_tecnico': form_tecnico, 'form_endereco': form_endereco})

def listar_tecnicos(request):
    tecnicos = tecnico_service.listar_tecnicos()
    return render(request, 'tecnicos/lista_tecnicos.html', {'tecnicos': tecnicos})

def listar_tecnico_id(request, id):
    tecnico = tecnico_service.listar_tecnico_id(id)
    return render(request, 'tecnicos/lista_tecnico.html', {'tecnico': tecnico})

def editar_tecnico(request, id):
    tecnico_editar = tecnico_service.listar_tecnico_id(id)
    tecnico_editar.data_nascimento = tecnico_editar.data_nascimento.strftime('%Y-%m-%d')
    form_tecnico = TecnicoForm(request.POST or None, instance=tecnico_editar)
    endereco_editar = endereco_service.listar_endereco_id(tecnico_editar.endereco.id)
    form_endereco = EnderecoTecnicoForm(request.POST or None, instance=endereco_editar)
    if form_tecnico.is_valid():
        nome = form_tecnico.cleaned_data["nome"]
        email = form_tecnico.cleaned_data["email"]
        cpf = form_tecnico.cleaned_data["cpf"]
        data_nascimento = form_tecnico.cleaned_data["data_nascimento"]
        profissao = form_tecnico.cleaned_data["profissao"]
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_editado = endereco_service.editar_endereco(endereco_editar, endereco_novo)
            tecnico_novo = tecnico.Tecnico(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_editado)
            tecnico_service.editar_tecnico(tecnico_editar, tecnico_novo)
            return redirect('listar_tecnicos')
    return render(request, 'tecnicos/form_tecnico.html', {'form_tecnico': form_tecnico ,'form_endereco': form_endereco})

def remover_tecnico(request, id):
    tecnico = tecnico_service.listar_tecnico_id(id)
    endereco = endereco_service.listar_endereco_id(tecnico.endereco.id)
    if request.method == "POST":
        tecnico_service.remover_tecnico(tecnico)
        endereco_service.remover_endereco(endereco)
        return redirect('listar_tecnicos')
    return render(request, 'tecnicos/confirma_exclusao.html', {'tecnico': tecnico})





