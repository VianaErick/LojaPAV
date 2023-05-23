from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
db = SQLAlchemy()

class Cliente(Base):
    __tablename__ = 'clientes'
    __table_args__ = {'extend_existing': True}
    
    idCliente = Column(Integer, primary_key=True, autoincrement=True)
    nomeCliente = Column(String(45), nullale=False)
    enderecoCliente = Column(String(255), default="", nullable=False)

    pedido = relationship("Pedido", back_populates='cliente')


class Jogo(Base):
    __tablename__ = 'jogos'
    __table_args__ = {'extend_existing': True}
    
    idJogo = Column(Integer, primary_key=True, autoincrement=True)
    nomeJogo = Column(String(45), nullale=False)
    descricaoJogo = Column(String(255), default="", nullable=False)
    categoriaJogo = Column(String(45), nullale=False)
    precoJogo = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates='jogo')

    nomeJogo_unique_constraint = UniqueConstraint(nomeJogo)

class Pedido(Base):
    __tablename__ = 'pedidos'
    __table_args__ = {'extend_existing': True}

    idPedido = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, ForeignKey('clientes.idCliente'), nullable=False)
    idJogo = Column(Integer, ForeignKey('jogos.idJogo'), nullable=False)
    dataPedido = Column(Date, nullable=False, nullable=False)
    precoPedido = Column(Float, nullable = False, nullable=False)

    cliente = relationship("Cliente", back_populates='pedido')
    jogo = relationship("Jogo", back_populates='pedido')


engine = create_engine('mysql://root:adm123@localhost:3306/SistemaAcademico2')
Base.metadata.create_all(engine)