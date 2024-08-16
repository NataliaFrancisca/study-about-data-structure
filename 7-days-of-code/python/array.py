class ListaDeCompras: 
    def __init__(self):
        self.items = []
        self.quantidade = []

    def adicionar_produto(self, nome, quantidade=None):
        if(nome == ''):
            print("Você precisa digitar o nome do produto")
            return False
        
        if(quantidade == None):
            self.quantidade.append(1)
        else:
            self.quantidade.append(quantidade)
        
        self.items.append(nome)
    
    def remove_produto(self, nome):
        if(nome == ''):
            print('Você precisa digitar o nome do produto')
            return 
        if nome not in self.items:
            print('Produto não encontrado')
            return

        indexProduto = self.items.index(nome)  
        self.items.pop(indexProduto)
        self.quantidade.pop(indexProduto)
    
    def exibirLista(self):
        for x in range(len(self.items)):
            print('PRODUTO:', self.items[x], '|', 'QUANTIDADE:', self.quantidade[x])


# LISTA DE COMPRAS
lista_123 = ListaDeCompras()

# ADICIONAR PRODUTOS
lista_123.adicionar_produto('Sabonete', 3)
lista_123.adicionar_produto('Shampoo')
lista_123.adicionar_produto('Arroz', 2)

lista_123.exibirLista();

# REMOVER PRODUTO
lista_123.remove_produto('Shampoo')

lista_123.exibirLista();