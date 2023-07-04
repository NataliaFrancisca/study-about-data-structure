// A PLAYLIST LINKED LIST 
// ADD A MUSIC 
// - ADD PREVIOUS/NEXT NODE

class Playlist{
    constructor(){
        this.head = this.tail = null
    };

    // add to the end of list / tails
    append(value){
        // check if the list is empty
        if(!this.tail){
            // tanto head e tail vão ser o novo valor
            this.head = this.tail = new Song(value);
        }else{
            // estou adicionando um novo valor, então preciso pegar o último valor que estava na lista
            let oldTail = this.tail;
            // definindo que o último valor agora vai ser o novo valor
            this.tail = new Song(value);
            // definindo que next agora vai ser igual ao novo valor
            oldTail.next = this.tail;
            // e que o prev no novo valor vai ser igual ao antigo valor
            this.tail.prev = oldTail;
        }
    }

    // remove the first element at the list
    deleteHead(){
        if(!this.head){
            return null;
        }else{
            let removedHead = this.head;
            // se só existe 1 elemento na minha lista, ele é head/tail => então preciso definir os dois como null
            if(this.head === this.tail){
                this.head = this.tail = null;
            }else{
                this.head = this.head.next;
                this.head.prev = null;
            }

            return removedHead;
        }
    }

    // remove the last element at the list
    deleteTail(){
        if(!this.tail){
            return null;
        }else{
            let removedTail = this.tails;

            // se só existe 1 elemento na minha lista, ele é head/tail => então preciso definir os dois como null
            if(this.head === this.tail){
                this.head = this.tail = null;
            }else{ // se existe mais elementos na minha lista, então...
                this.tail = this.tail.prev; // minha tail agora vai ser o meu previous element
                this.tail.next = null; // e meu next agora vai ser null, já que não tenho mais elementos a frente dele
            }

            return removedTail;
        }
    }

    deleteNode(value){
        let currentNode = this.head;

        while(currentNode){
            if(currentNode.value === value){
                const prev = currentNode.prev;
                const next = currentNode.next;

                if(!prev && !next){
                    this.head = this.tail = null;
                }

                if(prev && next){
                    prev.next = next;
                    next.prev = prev;
                }
                
                if(prev == null){
                    next.prev = null;
                    this.head = next;
                }

                if(next == null){   
                    prev.next = null
                    this.tail = prev;
                }

                return currentNode;
            }

            currentNode = currentNode.next;
        }

        return null;
    }

    print(){
        let currentNode = this.head;

        while(currentNode){
            console.log(`
                ⬅️  ${currentNode.prev ? currentNode.prev.value : "None"}
                ⭐ ${currentNode.value}
                ➡️  ${currentNode.next ? currentNode.next.value : "None"} 
            `)
            currentNode = currentNode.next;
        }

        return null;
    }

    search(value){
        let currentNode = this.head;

        while(currentNode){
            if(currentNode.value === value){
                console.log(currentNode);
                return currentNode;
            }

            currentNode = currentNode.next;
        }

        return null;
    }
}


class Song{
    constructor(value, prev, next){
        this.value = value;
        this.prev = prev || null;
        this.next = next || null;
    }
}


const nt_playlist = new Playlist();
nt_playlist.append('Medicine');
nt_playlist.append('Youth')
nt_playlist.append('20 ligações')
nt_playlist.append('Into In')

// console.log(nt_playlist.head);
// console.log(nt_playlist)

// nt_playlist.deleteTail();
// nt_playlist.deleteHead();
// nt_playlist.print();
// nt_playlist.deleteNode('Youth')
// nt_playlist.print();
// nt_playlist.deleteNode('20 ligações');
// nt_playlist.print();
// nt_playlist.deleteNode('Into In');
// nt_playlist.print();
// nt_playlist.search('Into In');

// delete the second element
// nt_playlist.deleteNode('Youth');

// delete the third element
// nt_playlist.deleteNode('20 ligações');

// delete the last element using delete node
// nt_playlist.deleteNode('Into In');

// delete the first element using delete node
nt_playlist.deleteNode('Medicine');

// nt_playlist.deleteNode('Medicine');
nt_playlist.print();
