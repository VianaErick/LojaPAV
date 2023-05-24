import sqlalchemy 
from sqlalchemy import Date, Float
from ..models.models import Pedido, Cliente, Jogo, db

def get_pedidos() -> sqlalchemy.orm.query.Query:
    pedidos = db.session.query(Pedido).all()
    return pedidos


def get_pedido(idPedido: int) -> Pedido:
    pedido = db.session.query(Pedido).get(idPedido)
    return pedido


def delete_pedido(idPedido: int):
    pedido = db.session.query(Pedido).get(idPedido)
    db.session.delete(pedido)
    db.session.commit()


def select_pedido(dataPedido: Date) -> sqlalchemy.orm.query.Query:
    print(dataPedido)
    pedido = db.session.query(Pedido).filter_by(dataPedido=dataPedido).all()
    return pedido


def add_pedido(idCliente: int, idJogo: int, dataPedido: Date, precoPedido: Float) -> Pedido:
    pedido = Pedido(idCliente=idCliente, idJogo=idJogo, dataPedido=dataPedido, precoPedido=precoPedido)
    db.session.add(pedido)

    db.session.commit()

    return pedido

def update_pedido(idPedido: int, idCliente: int, idJogo: str, dataPedido: Date, precoPedido: Float ) -> Pedido:
    pedido = db.session.query(Pedido).get(idPedido)
    
    pedido.idCliente = idCliente
    pedido.idJogo = idJogo
    pedido.dataPedido = dataPedido
    pedido.precoPedido = precoPedido

    db.session.commit()

    return pedido