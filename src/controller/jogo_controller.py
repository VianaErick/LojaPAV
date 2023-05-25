from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ..repository.jogos_repository import get_jogo, get_jogos, add_jogo, update_jogo, delete_jogo, select_jogo

response_fields = {
    "idJogo": fields.Integer,
    "nomeJogo": fields.String,
    "descricaoJogo": fields.String,
    "categoriaJogo": fields.String,
    "precoJogo": fields.Float,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("nomeJogo", type=str, help="", required=True)
request_parser.add_argument("descricaoJogo", type=str, help="", required=True)
request_parser.add_argument("categoriaJogo", type=str, help="", required=True)
request_parser.add_argument("precoJogo", type=float, help="", required=True)


class JogoItem(Resource):
    @marshal_with(response_fields)
    def get(self, idJogo):
        try:
            jogo = get_jogo(idJogo)
            if not jogo:
                abort(404, message="Resource not found")
            return jogo, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, idJogo):
        try:
            delete_jogo(idJogo)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, idJogo):
        try:
            args = request_parser.parse_args(strict=True)
            jogo = update_jogo(**args, idJogo=idJogo)
            return jogo, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class JogoList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_jogo(request.args['nomeJogo'])
            else:
                return get_jogos(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            jogo = add_jogo(**args)
            return jogo, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")