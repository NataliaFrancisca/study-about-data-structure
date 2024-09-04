class Node:
    def __init__(self, valor):
        self.valor =  valor
        self.proximo = None

def adicionarNo(lista, valor):
    atual = lista

    while(atual.proximo is not None):
        atual = atual.proximo

    atual.proximo = Node(valor)

def listar(lista):
    atual = lista

    while(atual):
        proximo = None

        if(atual.proximo is not None):
            proximo = atual.proximo.valor
        else:
            proximo = None

        print("NOME:", atual.valor, " ", "PROXIMO:", proximo)
        atual = atual.proximo

def remover(lista, valor):
    atual = lista
    anterior = None

    while(atual):
        proximo = atual.proximo

        if(atual.valor == valor):
            if(anterior is None):
                lista = proximo
                anterior = None
            else:
                anterior.proximo = proximo

        anterior = atual
        atual = proximo

    return lista

# Inicializando a lista:
listaDeNos = Node('Melly')

# Adicionando um novo valor
adicionarNo(listaDeNos, 'Liniker')

print(listaDeNos.valor) # Melly
print(listaDeNos.proximo.valor) # Liniker

# Adicionando um novo valor
adicionarNo(listaDeNos, "Duquesa")

print(listaDeNos.proximo.proximo.valor) # Duquesa

listar(listaDeNos) # Melly > Liniker > Duquesa
listaDeNos = remover(listaDeNos, 'Melly')
listar(listaDeNos) # Liniker > Duquesa