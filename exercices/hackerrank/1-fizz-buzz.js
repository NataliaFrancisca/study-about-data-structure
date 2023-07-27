function fizzBuzz(n) {
    // Write your code here
    for(let i = 1; i <= n; i++){
        const per3 = i % 3;
        const per5 = i % 5;

        if(per3 == 0 && per5 == 0){
            console.log("FizzBuzz");
        } else if(per3 == 0){
            console.log('Fizz');
        } else if(per5 == 0){
            console.log("Buzz")
        } else{
            console.log(i)
        }
    }
}

fizzBuzz(15);