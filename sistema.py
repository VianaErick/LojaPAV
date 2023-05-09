from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    
    idCliente = Column(Integer, primary_key=True)
    nomeCliente = Column(String)
    enderecoCliente = Column(String)

    pedido = relationship("Pedido", back_populates='cliente')


class Jogo(Base):
    __tablename__ = 'jogos'
    
    idJogo = Column(Integer, primary_key=True)
    nomeJogo = Column(String)
    descricaoJogo = Column(String)
    categoriaJogo = Column(String)
    precoJogo = Column(Float)

    pedido = relationship("Pedido", back_populates='jogo')

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    idPedido = Column(Integer, primary_key=True)
    idCliente = Column(Integer, ForeignKey('clientes.idCliente'))
    idJogo = Column(Integer, ForeignKey('jogos.idJogo'))

    cliente = relationship("Cliente", back_populates='pedido')
    jogo = relationship("Jogo", back_populates='pedido')

engine = create_engine('postgresql://postgres:12345@localhost:5432/pav')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


