from controller.cliente_controller import ClienteItem, ClienteList

def initialize_endpoints(api):
    api.add_resource(ClienteItem, "/clientes/<int:idCliente>")
    api.add_resource(ClienteList, "/clientes")