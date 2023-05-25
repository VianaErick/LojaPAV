import sqlalchemy
from ..models.models import Jogo, db

def get_jogos() -> sqlalchemy.orm.query.Query:
    jogos = db.session.query(Jogo).all()
    return jogos


def get_jogo(idJogo: int) -> Jogo:
    jogo = db.session.query(Jogo).get(idJogo)
    return jogo


def delete_jogo(idJogo: int):
    jogo = db.session.query(Jogo).get(idJogo)
    db.session.delete(jogo)
    db.session.commit()


def select_jogo(nomeJogo: str) -> sqlalchemy.orm.query.Query:
    print(nomeJogo)
    jogo = db.session.query(Jogo).filter_by(nomeJogo=nomeJogo).all()
    return jogo


def add_jogo(nomeJogo: str, descricaoJogo: str, categoriaJogo: str, precoJogo: float) -> Jogo:
    jogo = Jogo(nomeJogo=nomeJogo, descricaoJogo=descricaoJogo, categoriaJogo=categoriaJogo, precoJogo=precoJogo)
    db.session.add(jogo)

    db.session.commit()

    return jogo

def update_jogo(idJogo:int, nomeJogo: str, descricaoJogo: str, categoriaJogo: str, precoJogo: float) -> Jogo:
    jogo = db.session.query(Jogo).get(idJogo)
    
    jogo.nomeJogo = nomeJogo
    jogo.descricaoJogo = descricaoJogo
    jogo.categoriaJogo = categoriaJogo
    jogo.precoJogo = precoJogo

    db.session.commit()

    return jogo