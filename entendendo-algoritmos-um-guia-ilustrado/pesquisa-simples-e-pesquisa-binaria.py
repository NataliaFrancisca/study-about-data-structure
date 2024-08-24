listaDeNumeros = [1,2,3,4,5,6,7,8];
# listaDeNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

def buscaSimples(numeroParaBusca):
    numeroDeOperacoes = 0

    for x in listaDeNumeros:
        numeroDeOperacoes+=1

        if(x == numeroParaBusca):
            print("Achei o número: ", x)
            break

    print("Número de operações (Simples): ", numeroDeOperacoes)

def buscaBinaria(numeroParaBusca):
    numeroDeOperacoes = 0

    ponteiroInicio = 0
    ponteiroFinal = len(listaDeNumeros) - 1;

    while(ponteiroInicio <= ponteiroFinal):
        ponteiroMeio = int((ponteiroFinal + ponteiroInicio) / 2)

        if(listaDeNumeros[ponteiroMeio] == numeroParaBusca):
            print("Busca Binária: achei o número: ", listaDeNumeros[ponteiroMeio])
            break;

        if(numeroParaBusca > listaDeNumeros[ponteiroMeio]):
            ponteiroInicio = ponteiroMeio + 1
        
        if(numeroParaBusca < listaDeNumeros[ponteiroMeio]):
           ponteiroFinal = ponteiroMeio - 1

        numeroDeOperacoes+=1

    print("Número de operações (Binário): ", numeroDeOperacoes)



buscaSimples(8);
buscaBinaria(8);