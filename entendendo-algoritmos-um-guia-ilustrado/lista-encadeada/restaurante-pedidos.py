import random

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.id = random.randrange(1, 100)

class Pedido:
    def __init__(self, pedido, id, cliente):
        self.pedido = pedido
        self.id = id
        self.proximo = None
        self.cliente = Cliente(cliente)

class ListaPedidos:
    def __init__(self):
        self.cabeca = None
        self.numeroDePedidos = 0

    def atualizarNumeroDePedidos(self):
        self.numeroDePedidos = self.numeroDePedidos + 1

    def adicionar(self, pedido, cliente):
        if(self.cabeca is None):
            self.cabeca = Pedido(pedido, self.numeroDePedidos, cliente)
            self.atualizarNumeroDePedidos()
        else:
            pedidoAtual = self.cabeca

            # usando o while para passar entre os elementos até achar um pedido que tenha (proximo) como None
            # se houver um proximo > então atualizar o pedido atual
            while(pedidoAtual.proximo is not None):
                pedidoAtual = pedidoAtual.proximo
            
            # encontrou o último pedido da lista > adicionar um novo pedido
            pedidoAtual.proximo = Pedido(pedido, self.numeroDePedidos, cliente)
            self.atualizarNumeroDePedidos()
    
    def print(self):
        current = self.cabeca

        while(current):
            print("PEDIDO:", current.id, "~", current.pedido, "~", current.cliente.nome)
            current = current.proximo

    def remover(self, id):
        current = self.cabeca
        prev = None

        # usando o while para percorrer todos os elementos
        # vai percorrer até achar um pedido que tenha um ID igual ao parametro (id)
        while(current.proximo is not None):
            
            if(current.id == id):
                # encontrou o pedido
                # o pedido anterior agora tem o valor de proximo atualizado
                prev.proximo = current.proximo
                break
            
            # se não achou o valor, atualizar o prev e current
            # o prev é para que a gente consiga atualizar o proximo quando o id for encontrado
            prev = current
            current = current.proximo
        

pedidos = ListaPedidos()

pedidos.adicionar('Coxinha de camarão', 'Natalia')
pedidos.adicionar('Macarrão com molho branco', 'Natalia')
pedidos.adicionar('Cogumelos com arroz', 'Luiz')
pedidos.adicionar('Macarrão com molho branco', 'Maria')

pedidos.print()

pedidos.remover(2)

print('---------')

pedidos.print()

pedidos.adicionar('Coxinha de camarão', 'João')
pedidos.adicionar('Cogumelos com arroz', 'Maria')

print('---------')

pedidos.print()
# print(pedidos.cabeca.pedido)