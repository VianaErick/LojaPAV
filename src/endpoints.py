from .controller.cliente_controller import ClienteItem, ClienteList
from .controller.jogo_controller import JogoItem, JogoList
from .controller.pedido_controller import PedidoItem, PedidoList


def initialize_endpoints(api):
    api.add_resource(ClienteItem, "/clientes/<int:idCliente>")
    api.add_resource(ClienteList, "/clientes")
    api.add_resource(JogoItem, "/jogos/<int:idJogo>")
    api.add_resource(JogoList, "/jogos")
    api.add_resource(PedidoItem, "/pedidos/<int:idPedido>")
    api.add_resource(PedidoList, "/pedidos")