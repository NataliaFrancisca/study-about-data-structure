class Cliente{
    constructor(id, nome){
        this.id = id;
        this.nome = nome;
    }
}

class FilaAtendimento{
    constructor(){
        this.fila = [];
    }

    adicionar(id, nome){
        const cliente = new Cliente(id, nome); 
        this.fila.push(cliente);
    }

    remover(){
        if(this.fila.length == 0){
            console.log("Nenhum cliente para atender");
            return;
        }

        this.fila.shift();
    }

    listar(){
        if(this.fila.length == 0){
            console.log("Nenhum cliente para listar");
            return;
        }   

        console.log('🔍   LISTA DE PEDIDOS:');
        for(let x in this.fila){
            const { id, nome } = this.fila[x];
            console.table([{ID: id, NOME: nome.toUpperCase()}]);
        }
    }

    listar_primeiro_pedido(){
        if(this.fila.length == 0){
            console.log("Nenhum cliente para listar");
            return;
        }

        const { id, nome } = this.fila[0];
        console.log('🔍  PRIMEIRO PEDIDO:');
        console.table([{ID: id, NOME: nome.toUpperCase()}]);
    }
}

const dia_14_atendimentos = new FilaAtendimento();
dia_14_atendimentos.adicionar(1, 'natalia');
dia_14_atendimentos.adicionar(2, 'luiz');
dia_14_atendimentos.adicionar(3, 'bad bunny');

// dia_14_atendimentos.listar();
dia_14_atendimentos.remover();
dia_14_atendimentos.remover();
dia_14_atendimentos.listar();

dia_14_atendimentos.listar_primeiro_pedido();
dia_14_atendimentos.adicionar(22, 'maria');
dia_14_atendimentos.adicionar(4, 'karol g');
dia_14_atendimentos.listar();