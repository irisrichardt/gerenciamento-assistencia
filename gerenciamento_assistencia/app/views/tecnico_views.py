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


# def remover_cliente(request, id):
#     cliente = cliente_service.listar_cliente_id(id)
#     endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
#     if request.method == "POST":
#         cliente_service.remover_cliente(cliente)
#         endereco_service.remover_endereco(endereco)
#         return redirect('listar_clientes')
#     return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})




# def editar_cliente(request, id):
#     cliente_editar = cliente_service.listar_cliente_id(id)
#     cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d')
#     form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
#     endereco_editar = endereco_service.listar_endereco_id(cliente_editar.endereco.id)
#     form_endereco = EnderecoClienteForm(request.POST or None, instance=endereco_editar)
#     if form_cliente.is_valid():
#         nome = form_cliente.cleaned_data["nome"]
#         email = form_cliente.cleaned_data["email"]
#         cpf = form_cliente.cleaned_data["cpf"]
#         data_nascimento = form_cliente.cleaned_data["data_nascimento"]
#         profissao = form_cliente.cleaned_data["profissao"]
#         if form_endereco.is_valid():
#             rua = form_endereco.cleaned_data["rua"]
#             cidade = form_endereco.cleaned_data["cidade"]
#             estado = form_endereco.cleaned_data["estado"]
#             endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
#             endereco_editado = endereco_service.editar_endereco(endereco_editar, endereco_novo)
#             cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
#                                            profissao=profissao, cpf=cpf, endereco=endereco_editado)
#             cliente_service.editar_cliente(cliente_editar, cliente_novo)
#             return redirect('listar_clientes')
#     return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente ,'form_endereco': form_endereco})
