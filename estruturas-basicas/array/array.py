# Listas com diferentes tipos de dados
numeros = [1,2,3,4,5]
notas = [1.2, 2.4, 6.4]
frutas = ['Maça', 'Banana', 'Melancia']
objetos = [{'nome': 'João', 'idade': 12}, {'nome': 'Maria', 'idade': 14}]
respostas = [True, False, False, True]

# Percorrendo uma lista
for x in objetos:
    print('Aluno:', x['nome'])

# Tamanho de uma lista
tamanho = len(respostas)
print('Tamanho da Lista Respostas', tamanho)

# Buscar o primeiro elemento de uma lista
primeiroObj = objetos[0]
print('Primeiro Aluno', primeiroObj)

# Buscar o última elemento de uma lista
tamanhoLista = len(notas)
ultimaNota = notas[tamanhoLista - 1]
print('Última nota:', ultimaNota)

# Remove um elemento da lista
print("Lista antes de remover elemento", numeros)
numeros.remove(4)
print("Lista depois de remover elemento", numeros)

# Adiciona um elemento na lista
print("Lista antes de adicionar elemento", numeros)
numeros.append(6)
print("Lista depois de adicionar elemento", numeros)

# Retonar o index de um elemento
index = notas.index(2.4)
print("Index do elemento 2.4:", index)