let arr = [2, 5, 3, 4, 8, 1, 10, 6, 9];

for(let i = 0; i < arr.length; i++){ // percorrer todo o array
    for(let j = 0; j < (arr.length - i - 1); j++){ // percorrer todo o array mas começando do tamanho do array, e sempre diminuindo com o valor do contador i e -1
       if(arr[j] > arr[j + 1]){
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp; 
       }
    }
}

console.log(arr);
// arrlenght = 9
// i = 0 => 9 - 0 - 1 = 8
// i = 1 => 9 - 1 - 1 = 7
// i = 2 => 9 - 2 - 1 = 6
// i = 3 => 9 - 3 - 1 = 5
