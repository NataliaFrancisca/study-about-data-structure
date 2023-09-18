class ListaDeCompras{
    itens = [];
    quantidades = [];

    adicionar_item(nome_produto, quantidade){
        if(nome_produto == ''){
            console.log("Você precisa digitar o nome e quantidade do produto");
            return false;
        }

        this.itens.push(nome_produto);
        this.quantidades.push(quantidade);
    }

    remover_item(nome_produto){
        const produto_index = this.itens.indexOf(nome_produto);

        if(nome_produto == ''){
            console.log('Você precisa digitar o nome do produto');
            return false;
        }

        if(produto_index == -1){
            console.log('Produto não encontrado');
            return false;
        }

        this.itens.splice(produto_index, 1);
        this.quantidades.splice(produto_index, 1);
    }

    listar_itens(){
        for(let i = 0; i < this.itens.length; i++){
            console.log(`[PRODUTO]: ${this.itens[i]} - [QUANTIDADE]: ${this.quantidades[i]}`)
        }
    }

}


const lista_de_compras_natalia = new ListaDeCompras();

lista_de_compras_natalia.adicionar_item('maça', 4);
lista_de_compras_natalia.adicionar_item('arroz', 3);
lista_de_compras_natalia.adicionar_item('tortinha de brigadeiro', 10);
lista_de_compras_natalia.adicionar_item('leite integral', 12);
lista_de_compras_natalia.adicionar_item('', 2);

lista_de_compras_natalia.remover_item('leite integral');
lista_de_compras_natalia.remover_item('chocolate');
lista_de_compras_natalia.listar_itens();