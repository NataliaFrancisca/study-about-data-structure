class Livro{
    constructor(titulo, autor, paginas){
        this.titulo = titulo;
        this.autor = autor;
        this.paginas = paginas;
    }
}

class PilhaDeLivros{
    constructor(){
        this.pilhaLivros = [];
        // BOTTOM ---- TOP
    }

    adicionar(titulo, autor, paginas){
        let livro = new Livro(titulo, autor, paginas);
        this.pilhaLivros.push(livro);
    }

    remover(){
        if(this.pilhaLivros.length == 0){
            console.log("Não tem livros para remover");
            return;
        }

        this.pilhaLivros.pop();
    }

    listar(){
        if(this.pilhaLivros.length == 0){
            console.log("Não tem livros para listar");
            return;
        }

        for(let x in this.pilhaLivros){
            const {titulo, autor, paginas} = this.pilhaLivros[x];
            console.table([{titulo, autor, paginas}])
        }
    }
}

const pilha_um = new PilhaDeLivros();
pilha_um.adicionar('Pachinko', 'Min Jee Lee', 430);
pilha_um.adicionar('All about Love', 'Bell Hooks', 220);
pilha_um.adicionar('Amendoas', 'Sohn Won-pyung', 288);
pilha_um.listar();
pilha_um.remover();
pilha_um.listar();