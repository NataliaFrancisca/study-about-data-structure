class Song{
    constructor(id, title, artist){
        this.id = id;
        this.title = title;
        this.artist = artist;
        this.prev, this.next = null;
    }
}

class Playlist{
    constructor(){
        this.head, this.tail = null;
        this.size = 0;
    }

    size(){
        return this.size;
    }

    append(id, title, artist){
        this.size++;
        let node = this.head;

        if(this.head == null){
            this.head = this.tail = new Song(id, title, artist);
            return;
        }

        while(node.next){
            node = node.next;   
        }

        node.next = this.tail = new Song(id, title, artist);
        node.next.prev = node;
    }

    remove(id){
        let node = this.head;
        this.size--;

        // IF I'M TRYING TO REMOVE THE HEAD NODE
        if(this.head.id == id){
            let newHead = this.head.next;
            newHead.prev = null;
            this.head = newHead;
            return;
        }

        // IF I'M TRYING TO REMOVE THE TAIL NODE
        if(this.tail.id == id){
            let newTail = this.tail.prev;
            newTail.next = null;
            this.tail = newTail;
            return;
        }


        while(node){
            if(node.id == id){
                const prev = node.prev;
                const next = node.next;
                prev.next = next;
                next.prev = prev;
                return;
            }

            node = node.next;
        }
        
        console.log("There is no song with this ID");
    }


    list(){
        let node = this.head;

        if(this.head == null){
            console.log("There are no songs registered");
            return;
        }

        while(node){
            const { id, title, next, prev } = node;
            console.table([{id: id, previous: prev ? prev.title : null, playing: title, next: next ? next.title : null}]);
            node = node.next;
        }
    }

    access_song(idx){
        let node = this.head;

        if(this.head == null){
            console.log('There are no songs registered');
            return;
        }

        while(node){
            const { id, title, artist} = node;
            
            if(id == idx){
                console.table([{ID: id, SONG: title, ARTIST: artist}]);
                return;
            }
        }
    }

}

const playlist_nt = new Playlist();
playlist_nt.append(1, 'Cartas para Amy', 'Black Alien');
playlist_nt.append(2, 'Fica até umas horas', 'Black Alien');
playlist_nt.append(3, 'Dejavu', 'Olivia Rodrigo');
playlist_nt.append(7, 'Another Love', 'Marco');

playlist_nt.remove(2);
playlist_nt.remove(3);
// playlist_nt.list();

playlist_nt.access_song(1);