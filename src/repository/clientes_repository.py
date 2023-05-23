import sqlalchemy
from models.models import Cliente, db

def get_clientes() -> sqlalchemy.orm.query.Query:
    clientes = db.session.query(Cliente).all()
    return clientes


def get_cliente(idCliente: int) -> Cliente:
    cliente = db.session.query(Cliente).get(idCliente)
    return cliente


def delete_cliente(idCliente: int):
    cliente = db.session.query(Cliente).get(idCliente)
    db.session.delete(cliente)
    db.session.commit()


def select_cliente(nomeCliente: str) -> sqlalchemy.orm.query.Query:
    print(nomeCliente)
    cliente = db.session.query(Cliente).filter_by(nomeCliente=nomeCliente).all()
    return cliente


def add_cliente(nomeCliente: str, enderecoCliente: str) -> Cliente:
    cliente = Cliente(nomeCliente=nomeCliente, enderecoCliente=enderecoCliente)
    db.session.add(cliente)

    db.session.commit()

    return cliente

def update_cliente(nomeCliente: str, enderecoCliente: str, idCliente: int) -> Cliente:
    cliente = db.session.query(Cliente).get(idCliente)
    
    cliente.nomeCliente = nomeCliente
    cliente.enderecoCliente = enderecoCliente

    db.session.commit()

    return cliente