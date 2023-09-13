const hash = (key, size) => {
    let hashedKey = 0;

    for(let i = 0; i < key.length; i++){
        hashedKey += key.charCodeAt(i);
    }

    return hashedKey % size;
}

class HashTable{

    constructor(){
        this.size = 20
        this.buckets = Array(this.size) // buckets são os index do array, nesse temos 20

        for(let i = 0; i < this.buckets.length; i++){
            this.buckets[i] = new Map();
        }
    }

    // ESSE INSERT NÃO ESTÁ EVITANDO COLISÕES ENTRE KEYS
    // SÓ ESTÁ ADICIONANDO OS VALORES EM UM ARRAY
    insert(key, value){
        let index = hash(key, this.size); // deve sempre retornar o mesmo valor para a chave que estou passando

        // verificar se já está sendo usado essa chave
        if(this.buckets[index].has(key)){
            const currentValue = (this.buckets[index].get(key));
            let base = Array();

            if(Array.isArray(currentValue)){
                base.push(...currentValue);
            }else{
                base.push(currentValue);
            }
      
            this.buckets[index].set(key, base.concat(value));
        }else{
            this.buckets[index].set(key, value);
        }
    }

    delete(key){
        let index = hash(key, this.size); // deve sempre retornar o mesmo valor para a chave que estou passando
        let deleted = this.buckets[index].get(key);
        this.buckets[index].delete(key);
        return deleted;
    }

    search(key){
        let index = hash(key, this.size);
        return this.buckets[index].get(key);
    }

}

const hashHoy = new HashTable();
hashHoy.insert('30 seconds to mars', 'its war')
hashHoy.insert('olivia rodrigo', 'dejavu')
hashHoy.insert('muse', 'supermassive black hole')
hashHoy.insert('olivia rodrigo', 'hate u')
hashHoy.insert('olivia rodrigo', 'pretty')
console.log(hashHoy.buckets);
const search = hashHoy.search('olivia rodrigo')
console.log(search)


  
//     search(key) {
//       let idx = hash(key, this.size)
//       return this.buckets[idx].get(key)
//     }
//   }


// const teste1 = hash('30 seconds to mars', 20);
// const teste2 = hash('olivia rodrigo', 20);
// console.log(teste1);
// console.log(teste2);