// this way using linear-search
function linearSearch(arr, target){
    arr = sortArr(arr);
    let indexes = [];
    let operations = 0;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] === target){
            indexes.push(i);
        }

        operations++;
    }

    console.log("OP", operations);
    return indexes;
}

// USING LINEAR SEARCH BUT BREAKING THE CODE WHEN THE NEXT VALUE IN ARRAY IS BIGGER THAN THE TARGET
function searchTeste(arr, target){
    // could use the javascript .sort method
    arr = sortArr(arr);
    let indexes = [];
    let operations = 0;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] === target){
            indexes.push(i);
        }

        if(arr[i+1] > target){
            break;
        }

        operations++;
    }

    console.log("OP", operations);
    return indexes;
}

// FUNCTION TO SORT AN ARRAY
function sortArr(arr){
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < (arr.length - i - 1); j++){ 
           if(arr[j] > arr[j + 1]){
            let temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp; 
           }
        }
    }

    return arr;
}

// const b = linearSearch([1,2,5,2,2], 2);
// const c = searchTeste([1,2,5,2,2], 2);
// const b = binarySearch([1,2,5,2,3], 3);
// const c = binarySearch([1,2,5,2,3], 5);

// console.log(a);
// console.log(b);
// console.log(c);