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

    return arrayPairs;
}

class Game{
    constructor(){
        this.table = {};
    }

    append(player){
        this.table[player] = 0;
    }

    update(player, points){
        if(!this.table[player]){
            console.log("There are no players registered");
            return;
        }

        this.table[player] += points;
    }

    delete(player){
        if(!this.table[player]){
            console.log("There are no players registered");
            return;
        }

        delete this.table[player];
    }

    list(){
        const arr_sort = sort(this.table);

        if(arr_sort.length == 0){
            console.log("There are no players registered");
            return;
        }

        const obj_final = Object.fromEntries(arr_sort);
        for(let player in obj_final){
            console.log(`| ${player.toUpperCase()}: ${this.table[player]} `)
        }
    }

    winner(){
        const arr_sort = sort(this.table);

        if(arr_sort.length == 0){
            console.log("There are no players registered");
            return;
        }

        const winner = arr_sort[0];
        console.log(`🎉 WINNER: ${winner[0].toUpperCase()} - POINTS: ${winner[1]}`)
    }
}

const game = new Game();

game.append('natalia');
game.append('luiz');
game.append('gustavo');
game.append('leia');
game.append('olivia rodrigo');
game.append('chris');
game.list();

game.update('natalia', 20);
game.update('luiz', 10);
game.update('chris', 100);
game.list();
game.winner();