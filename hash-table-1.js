function sort(list){
    const arrayPairs = Object.entries(list);

    arrayPairs.sort((a,b) => {
        const valorA = a[1];
        const valorB = b[1];

        if (valorA > valorB) {
            return -1;
        }
        if (valorA < valorB) {
            return 1;
        }
        return 0;
    })

    return { 
        object: Object.fromEntries(arrayPairs),
        array: arrayPairs
    }
}

class HashTable{
    constructor(){
        this.table = {}
    }

    append(player){
        this.table[player] = 0;
    }
    
    update(player, points ){
        this.table[player] += points;
    }

    delete(player){
        delete this.table[player];
    }

    list(){
        const sort = sort(this.table);
        const obj = sort.object;
        for(let player in obj){
            console.log(`| ${player.toUpperCase()}: ${this.table[player]} `)
        }
    }

    winner(){
        const sortOjb = sort(this.table);
        const arr = sortOjb.array[0];
        console.log(`🎉 WINNER: ${arr[0].toUpperCase()} - POINTS: ${arr[1]}`)
    }

}

const game = new HashTable();
game.append('natalia');
game.append('luiz');
game.append('gustavo');
game.append('leia');
game.append('olivia rodrigo');
game.append('chris');

game.update('natalia', 20);
game.update('luiz', 10);
game.update('chris', 100);

game.delete('luiz');
// console.log(game.table);
// game.list();
game.winner();