listaDeNumerosPequena = [1,2,3,4,5,6,7,8];
listaDeNumerosGrande = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

def buscaSimples(lista, numeroParaBusca):
    numeroDeOperacoes = 0

    for x in lista:
        numeroDeOperacoes+=1

        if(x == numeroParaBusca):
            print("Busca Simples: achei o número: ", x)
            break

    print("Número de operações (Simples): ", numeroDeOperacoes)

def buscaBinaria(lista, numeroParaBusca):
    numeroDeOperacoes = 0

    ponteiroInicio = 0
    ponteiroFinal = len(lista) - 1;

    while(ponteiroInicio <= ponteiroFinal):
        ponteiroMeio = int((ponteiroFinal + ponteiroInicio) / 2)

        if(lista[ponteiroMeio] == numeroParaBusca):
            print("Busca Binária: achei o número: ", lista[ponteiroMeio])
            break;

        if(numeroParaBusca > lista[ponteiroMeio]):
            ponteiroInicio = ponteiroMeio + 1
        
        if(numeroParaBusca < lista[ponteiroMeio]):
           ponteiroFinal = ponteiroMeio - 1

        numeroDeOperacoes+=1

    print("Número de operações (Binário): ", numeroDeOperacoes)



buscaSimples(listaDeNumerosPequena, 8)
buscaBinaria(listaDeNumerosPequena, 8)
print("\n")
buscaSimples(listaDeNumerosGrande, 17)
buscaBinaria(listaDeNumerosGrande, 17)