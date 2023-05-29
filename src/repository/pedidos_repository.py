import sqlalchemy
from ..models.models import Pedido, db
from datetime import datetime

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


def select_pedido(dataPedido: str) -> sqlalchemy.orm.query.Query:
    date = datetime.strptime(dataPedido, "%Y-%m-%d")
    pedido = db.session.query(Pedido).filter_by(dataPedido=date).all()
    return pedido


def add_pedido(idCliente: int, idJogo: int, dataPedido: datetime, precoPedido: float) -> Pedido:
    pedido = Pedido(idCliente=idCliente, idJogo=idJogo, dataPedido=dataPedido, precoPedido=precoPedido)
    db.session.add(pedido)

    db.session.commit()

    return pedido

def update_pedido(idPedido: int, idCliente: int, idJogo: str, dataPedido: str, precoPedido: float ) -> Pedido:
    pedido = db.session.query(Pedido).get(idPedido)

    date = datetime.strptime(dataPedido, "%Y-%m-%d")
    
    pedido.idCliente = idCliente
    pedido.idJogo = idJogo
    pedido.dataPedido = date
    pedido.precoPedido = precoPedido

    db.session.commit()

    return pedido