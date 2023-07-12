class Pedido:
    def __init__(self, numero, cliente, itens, valor):
        self.numero = numero;
        self.cliente = cliente;
        self.itens = itens;
        self.valor = valor;

class ListaPedidos:
    def __init__(self):
        self.lista = [];
        
    def adicionar(self, pedido):
        self.lista.append(pedido);
    def remover(self):
        if len(self.lista) == 0:
            print("Nenhum pedido para remover")
        else:
            self.lista.pop(0);
    def listar(self):
        if len(self.lista) == 0:
            print("Nenhum pedido na lista")
        else:
            for x in self.lista:
                print(x.numero, x.cliente);
    def listar_primeiro_pedido(self):
        print(self.lista[0].cliente) if len(self.lista) > 0 else print("Nenhum pedido na lista")

onze_julho_2023_pedidos = ListaPedidos();

pedido_1 = Pedido(1, 'Natalia', ['Batata Frita', 'Hamburguer', 'Coca-Cola'], 45);
pedido_2 = Pedido(2, 'Luiz', ['Batata Frita', 'Coca-Cola'], 25);
pedido_3 = Pedido(3, 'Matheus', ['Hamburguer', 'Batata Frita', 'Coxinha', 'Bauru', 'Soda'], 100);

onze_julho_2023_pedidos.adicionar(pedido_1);
onze_julho_2023_pedidos.adicionar(pedido_2);
onze_julho_2023_pedidos.adicionar(pedido_3)

onze_julho_2023_pedidos.listar();
# onze_julho_2023_pedidos.remover();
# onze_julho_2023_pedidos.remover();
# onze_julho_2023_pedidos.listar();
onze_julho_2023_pedidos.listar_primeiro_pedido();
