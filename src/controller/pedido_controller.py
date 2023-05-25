from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.pedidos_repository import get_pedido, get_pedidos, add_pedido, update_pedido, delete_pedido, select_pedido

response_fields = {
    "idPedido": fields.Integer,
    "idCliente": fields.Integer,
    "idJogo": fields.Integer,
    "dataPedido": fields.String,
    "precoPedido": fields.Float,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("idCliente", type=int, help="", required=True)
request_parser.add_argument("idJogo", type=int, help="", required=True)
request_parser.add_argument("dataPedido", type=str, help="", required=True)
request_parser.add_argument("precoPedido", type=float, help="", required=True)


class PedidoItem(Resource):
    @marshal_with(response_fields)
    def get(self, idPedido):
        try:
            pedido = get_pedido(idPedido)
            if not pedido:
                abort(404, message="Resource not found")
            return pedido, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, idPedido):
        try:
            delete_pedido(idPedido)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, idPedido):
        try:
            args = request_parser.parse_args(strict=True)
            pedido = update_pedido(**args, idPedido=idPedido)
            return pedido, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class PedidoList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_pedido(request.args['dataPedido'])
            else:
                return get_pedidos(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            pedido = add_pedido(**args)
            return pedido, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")