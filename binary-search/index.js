var doSearch = function(array, targetValue) {
	var min = 0;
	var max = array.length - 1;
    var guess;

    if(max < min){
        return -1;
    }

    while(min - 1 < max){
        guess = Math.floor((min + max) / 2);

        if(array[guess] === targetValue){
            return guess;
        }

        if(array[guess] < targetValue){
            min = guess + 1;
        }

        if(array[guess] > targetValue){
            max = guess - 1;
        }
    }

	return -1;
};

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var result = doSearch(primes, 29);

console.log('result', result);