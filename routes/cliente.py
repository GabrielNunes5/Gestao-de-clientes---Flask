from flask import Blueprint, render_template, request
from database.models.cliente import Cliente


cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')
def lista_clientes():
    '''Listar os clientes'''
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST', ])
def inserir_cliente():
    '''Inserir os dados do cliente no servidor'''
    data = request.json

    novo_usuario = Cliente.create(nome=data['nome'], email=data['email'],)

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    '''Renderiza um form para criar um cliente'''
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    '''Exibir detalhes do cliente'''

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def editar_cliente(cliente_id):
    '''Formulario para editar um cliente'''
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    '''Atualizar informações do cliente'''
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''Deletar  cliente'''
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}