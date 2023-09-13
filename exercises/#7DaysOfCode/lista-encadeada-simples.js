class Paciente{
    constructor(nome, identificacao, status){
        this.nome = nome;
        this.identificacao = identificacao;
        this.status = status;
        this.next = null;
    }
};

class Pacientes {
    constructor(head = null) {
        this.head = head
        this.counter = 0;
    }

    size(){
        return this.counter;
    }

    adicionar(nome, id, status){
        let node = this.head;
        this.counter++;

        if(this.head == null){
            this.head = new Paciente(nome, id, status);
            return;
        }

        while(node.next){
            node = node.next;
        }

        node.next = new Paciente(nome, id, status);
    }


    remover(id){
        let node = this.head;
        this.counter--;

        // IF I'M TRYING TO REMOVE THE HEAD VALUE
        if(this.head.identificacao === id){
            this.head = node.next;
            return;
        }
        
        while(node.next){
            let prev_node = node;
            let next_node = prev_node.next;

            // IF THE VALUE THAT I'M TRYING TO REMOVE DOESNT HAVE A NEXT NODE
            if(next_node.identificacao == id && next_node.next == null){
                prev_node.next = null;
                return;
            }
            
            if(next_node.identificacao == id){
                prev_node.next = next_node.next;
            }

            node = node.next;
        }
    }

    listar(){
        let node = this.head;

        if(this.head == null){
            console.log("There are no pacients to list");
            return;
        }

        while(node.next){
            const { nome, identificacao, status } = node;
            console.log("\n", `[ID]: ${identificacao} [PACIENTE]: ${nome}, [STATUS]: ${status}`, "\n");
            node = node.next;
        }

    }

    acessar_paciente(id){
        let node = this.head;

        while(node.next){

            if(node.identificacao == id){
                const { nome, identificacao, status } = node;
                console.log("\n", `[ID]: ${identificacao} [PACIENTE]: ${nome}, [STATUS]: ${status}`, "\n");
                return;
            }
          
            node = node.next;
        }

        console.log("This pacient doesn't exist here");
    }
    
}

let lista_pacientes = new Pacientes();
lista_pacientes.adicionar('natalia', 1, 'estável');
lista_pacientes.adicionar('luiz', 2, 'estável');
lista_pacientes.adicionar('jasmine', 3, 'estável');
lista_pacientes.adicionar('claudias', 34, 'estável');

lista_pacientes.listar();

lista_pacientes.remover(34);
lista_pacientes.remover(3);
lista_pacientes.remover(1);
lista_pacientes.listar();

lista_pacientes.acessar_paciente(1);

