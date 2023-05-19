from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from controllers.lojaController import db

Base = declarative_base()

engine = create_engine('postgresql://postgres:12345@localhost:5432/pav')

class Cliente(db.Base):
    __tablename__ = 'clientes'
    __table_args__ = {'extend_existing': True}
    
    idCliente = Column(Integer, primary_key=True, autoincrement=True)
    nomeCliente = Column(String)
    enderecoCliente = Column(String)

    pedido = relationship("Pedido", back_populates='cliente')


class Jogo(db.Base):
    __tablename__ = 'jogos'
    __table_args__ = {'extend_existing': True}
    
    idJogo = Column(Integer, primary_key=True, autoincrement=True)
    nomeJogo = Column(String)
    descricaoJogo = Column(String)
    categoriaJogo = Column(String)
    precoJogo = Column(Float)

    pedido = relationship("Pedido", back_populates='jogo')

class Pedido(db.Base):
    __tablename__ = 'pedidos'
    __table_args__ = {'extend_existing': True}

    idPedido = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, ForeignKey('clientes.idCliente'))
    idJogo = Column(Integer, ForeignKey('jogos.idJogo'))
    dataPedido = Column(Date, nullable=False)
    precoPedido = Column(Float, nullable = False)

    cliente = relationship("Cliente", back_populates='pedido')
    jogo = relationship("Jogo", back_populates='pedido')


Base.metadata.create_all(engine)

