import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from sqlalchemy import text

load_dotenv()

lojaController = Flask(__name__)
lojaController.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/pav'
db = SQLAlchemy()
db.init_app(lojaController)

@lojaController.post("/api/cliente")
def create_cliente():
    data = request.get_json()
    nomeCliente = data["nomeCliente"]
    enderecoCliente = data["enderecoCliente"]

    insert_cliente_query = text("INSERT INTO clientes(nomeCliente, enderecoCliente) VALUES (:nomeCliente, :enderecoCliente)")
    db.session.execute(insert_cliente_query, {"nomeCliente": nomeCliente, "enderecoCliente": enderecoCliente})
    db.session.commit()

    idCliente = db.session.execute(text("SELECT LASTVAL();")).fetchone()[0]

    db.session.close()

    return {"id": idCliente, "message": f"{nomeCliente} criado."}, 201

@lojaController.get('/api/cliente')
def getall_cliente():
    from src.loja import Cliente
    
    clientes = db.session.query(Cliente).all()

    cliente_list = []
    for cliente in clientes:
        cliente_data = {
        "id": cliente.idCLiente,
        "nome": cliente.nomeCliente,
        "endereco": cliente.enderecoCliente,

        }
        cliente_list.append(cliente_data)

    db.session.close()

    return {"clientes": cliente_list}

@lojaController.get("/api/cliente/<idCliente>")
def get_cliente(idCliente):
    from src.loja import Cliente

    cliente = db.session.get(Cliente, idCliente)
    if cliente:
        return {
            "id": cliente.idCliente,
            "nome": cliente.nomeCliente,
            "endereco": cliente.enderecoCliente,
        }
    else:
        return {"message": "Cliente não encontrado"}, 404
    
@lojaController.put('/api/cliente/<idCliente>')
def put_cliente(idCliente):
    from src.loja import Cliente

    cliente = db.session.get(Cliente, idCliente)
    if cliente:
        data = request.get_json()
        cliente.nome = data["nomeCliente"]
        cliente.endereco = data["enderecoCliente"]
        db.session.commit()

        return {"message": f"Cliente {cliente.nomeCliente} atualizado."}
    else:
        return {"message": "Cliente não encontrado."}, 404
    
@lojaController.delete('/api/cliente/<idCliente>')
def del_cliente(idCliente):
    from src.loja import Cliente

    cliente = db.session.get(Cliente, idCliente)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()

        return {"message": f"Cliente {cliente.nomeCliente} deletado."}
    else:
        return {"message": "Cliente não encontrado."}, 404


@lojaController.post("/api/jogo")
def create_jogo():
    data = request.get_json()
    nomeJogo = data["nomeJogo"]
    descricaoJogo = data["descricaoJogo"]
    categoriaJogo = data["categoriaJogo"]
    precoJogo = data["precoJogo"]
    

    insert_jogo_query = text("INSERT INTO jogos(nomeJogo, descricaoJogo, categoriaJogo, precoJogo) VALUES (:nomeJogo, :descricaoJogo, :categoriaJogo, :precoJogo)")
    db.session.execute(insert_jogo_query, {"nomeJogo": nomeJogo, "descricaoJogo": descricaoJogo, "categoriaJogo": categoriaJogo, "precoJogo": precoJogo})
    db.session.commit()

    idJogo = db.session.execute(text("SELECT LASTVAL();")).fetchone()[0]

    db.session.close()

    return {"id": idJogo, "message": f"{nomeJogo} criado."}, 201  

@lojaController.get('/api/jogo')
def getall_jogo():
    from src.loja import Jogo
    
    jogos = db.session.query(Jogo).all()

    jogo_list = []
    for jogo in jogos:
        jogo_data = {
        "idJogo": jogo.idJogo,
        "nomeJogo": jogo.nomeJogo,
        "descricaoJogo": jogo.descricaoJogo,
        "categoriaJogo": jogo.categoriaJogo,
        "precoJogo": jogo.precoJogo    
        }
        jogo_list.append(jogo_data)

    db.session.close()

    return {"jogos": jogo_list}

@lojaController.get("/api/jogo/<idJogo>")
def get_jogo(idJogo):
    from src.loja import Jogo

    jogo = db.session.get(Jogo, idJogo)
    if jogo:
        return {
            "idJogo": jogo.idJogo,
            "nomeJogo": jogo.nomeJogo,
            "descricaoJogo": jogo.descricaoJogo,
            "categoriaJogo": jogo.categoriaJogo,
            "precoJogo": jogo.precoJogo,            
        }
    else:
        return {"message": "Jogo não encontrado"}, 404

@lojaController.put('/api/jogo/<idJogo>')
def put_jogo(idJogo):
    from src.loja import Jogo

    jogo = db.session.get(Jogo, idJogo)
    if jogo:
        data = request.get_json()
        jogo.nomeJogo = data["nomeJogo"]
        jogo.descricaoJogo = data["descricaoJogo"]
        jogo.categoriaJogo = data["categoriaJogo"]
        jogo.precoJogo = data["precoJogo"] 
        db.session.commit()

        return {"message": f"{jogo.nomeJogo} atualizado."}
    else:
        return {"message": "Jogo não encontrado."}, 404

@lojaController.delete('/api/jogo/<idJogo>')
def del_jogo(idJogo):
    from src.loja import Jogo

    jogo = db.session.get(Jogo, idJogo)
    if jogo:
        db.session.delete(jogo)
        db.session.commit()

        return {"message": f"{jogo.nomeJogo} deletado."}
    else:
        return {"message": "Jogo não encontrado."}, 404


@lojaController.post("/api/pedido")
def create_pedido():
    data = request.get_json()
    idPedido = data["idPedido"]
    idCliente = data["idCliente"]
    idJogo = data["idJogo"]
    dataPedido = data["dataPedido"]
    precoPedido = data["precoPedido"]

    

    insert_pedido_query = text("INSERT INTO pedidos(idPedido, idCliente, idJogo, dataPedido, precoPedido) VALUES (:idPedido, :idCliente, :idJogo, :dataPedido, :precoPedido)")
    db.session.execute(insert_pedido_query, {"idPedido": idPedido, "idCliente": idCliente, "idJogo": idJogo, "dataPedido": dataPedido, "precoPedido": precoPedido})
    db.session.commit()

    idJogo = db.session.execute(text("SELECT LASTVAL();")).fetchone()[0]

    db.session.close()

    return {"id": idJogo, "message": f"{idPedido} Criado."}, 201  

@lojaController.get('/api/pedido')
def getall_pedido():
    from src.loja import Pedido
    
    pedidos = db.session.query(Pedido).all()

    pedido_list = []
    for pedido in pedidos:
        pedido_data = {
        "idPedido": pedido.idPedido,
        "idCliente": pedido.idCliente,
        "idJogo": pedido.idJogo,
        "dataPedido": pedido.dataPedido,
        "precoPedido": pedido.precoPedido,     
        }
        pedido_list.append(pedido_data)

    db.session.close()

    return {"pedidos": pedido_list}

@lojaController.get("/api/pedido/<idPedido>")
def get_pedido(idPedido):
    from src.loja import Pedido

    pedido = db.session.get(Pedido, idPedido)
    if pedido:
        return {
            "idPedido": pedido.idPedido,
            "idCliente": pedido.idCliente,
            "idJogo": pedido.idJogo,
            "dataPedido": pedido.dataPedido,
            "precoPedido": pedido.precoPedido,                   
        }
    else:
        return {"message": "Pedido não encontrado"}, 404

@lojaController.put('/api/pedido/<idPedido>')
def put_pedido(idPedido):
    from src.loja import Pedido

    pedido = db.session.get(Pedido, idPedido)
    if pedido:
        data = request.get_json()
        pedido.idPedido = data["idPedido"]
        pedido.idCliente = data["idCliente"]
        pedido.idJogo = data["idJogo"]
        pedido.dataPedido = data["dataPedido"]
        pedido.precoPedido = data["precoPedido"]
        db.session.commit()

        return {"message": f"Pedido {pedido.idPedido} atualizado."}
    else:
        return {"message": "Pedido não encontrado."}, 404

@lojaController.delete('/api/pedido/<idPedido>')
def del_pedido(idPedido):
    from src.loja import Pedido

    pedido = db.session.get(Pedido, idPedido)
    if pedido:
        db.session.delete(pedido)
        db.session.commit()

        return {"message": f"Pedido {pedido.idPedido} deletado."}
    else:
        return {"message": "Pedido não encontrado."}, 404

if __name__ == "__main__":
    lojaController.run()