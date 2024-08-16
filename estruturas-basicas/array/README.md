# Array

Um array é uma **estrutura de dados linear** que armazena uma coleção de elementos de forma seguida na memória, um do lado do outro. Cada elemento em um array é identificado por um índice, o que permite o acesso direto e rápido aos elementos

Arrays são úteis quando você sabe de antemão quantos elementos precisa armazenar e deseja um acesso rápido a esses elementos.

![array](https://media.geeksforgeeks.org/wp-content/uploads/20240410101419/Getting-Started-with-Array-Data-Structure.webp)

| Na parte de indices, precisamos lembrar que eles começam pelo número 0 e assim por diante.


## Exemplo prático:

Vamos usar um array (lista, em Python) quando precisamos armazenar múltiplos valores que pertencem ao mesmo grupo ou que compartilham o mesmo tipo de dado.

**Exemplo:** Suponha que queremos armazenar os nomes de várias frutas. Como podemos fazer isso? Poderíamos armazenar cada fruta em uma variável separada, mas o que acontece se precisarmos remover ou adicionar uma nova fruta?

- **criando uma nova fruta como variável individual:** Para adicionar uma nova fruta, você teria que criar uma variável separada para essa fruta e, depois, utilizá-la de forma independente.
- **usando listas:** Com listas, você pode facilmente adicionar uma nova fruta à lista ou remover uma existente. Isso torna o gerenciamento de múltiplos itens muito mais eficiente e organizado.
  

```python

    # variaveis das frutas
    maca = 'Maça'
    banana = 'Banana'
    melancia = 'Melancia'

    # lista de frutas
    frutas = ['Maça', 'Banana', 'Melancia']

    # adicionar uma nova fruta
    frutas.append('Morango')

    # remover uma fruta
    frutas.remove('Maça')

```
- **flexibilidade e manipulação:** usar uma lista (frutas) é mais flexível, pois permite manipular as frutas em conjunto, adicionar novas frutas facilmente, ou realizar operações como ordenar ou filtrar.

## Alocação de memória:

### variável:

- cada uma dessas variáveis **`(maca, banana, melancia)`** é uma referência para um objeto str armazenado na memória.
- **cada variável armazena uma referência (um ponteiro) para a localização da string correspondente na memória**. Ou seja, **`maca`** aponta para uma posição de memória onde **`‘Maça’`** está armazenada, e assim por diante.

### listas:

- a lista **`frutas`** é um objeto de coleção que armazena referências para os mesmos objetos **`str`** (**`'Maça'`, `'Banana'`, `'Melancia'`**) que as variáveis individuais fariam.
- a lista em si é um objeto separado na memória que contém referências (ponteiros) para as strings. **Cada elemento da lista é, na verdade, uma referência a um objeto `str` armazenado em outro lugar na memória.**
