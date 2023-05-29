from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.clientes_repository import get_cliente, get_clientes, add_cliente, update_cliente, delete_cliente, select_cliente

response_fields = {
    "idCliente": fields.Integer,
    "nomeCliente": fields.String,
    "enderecoCliente": fields.String,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("nomeCliente", type=str, help="", required=True)
request_parser.add_argument("enderecoCliente", type=str, help="", required=True)


class ClienteItem(Resource):
    @marshal_with(response_fields)
    def get(self, idCliente):
        try:
            cliente = get_cliente(idCliente)
            if not cliente:
                abort(404, message="Resource not found")
            return cliente, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, idCliente):
        try:
            delete_cliente(idCliente)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, idCliente):
        try:
            args = request_parser.parse_args(strict=True)
            cliente = update_cliente(**args, idCliente=idCliente)
            return cliente, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class ClienteList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if  request.args:
                nomeCliente = request.args['nomeCliente']
                clientes = select_cliente(nomeCliente)
                return clientes, 200
            else:
                clientes = get_clientes()
                return clientes, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            cliente = add_cliente(**args)
            return cliente, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")