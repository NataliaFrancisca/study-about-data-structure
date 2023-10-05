const arr = [1,2,3,4,5];
let head = null;

class Node{
    constructor(value = null, next = null){
        this.value = value;
        this.next = next;
    }
}

function initialize(value){
    let node = head;

    if(node == null){
        head = new Node(value);
        return;
    }

    while(node.next){
        node = node.next;
    }

    node.next = new Node(value);
}

for(let i = 0; i < arr.length; i++){
    initialize(arr[i]);
}


function reverse(head){
    let current = head;
    let prev = null;

    while(current){
       let next = current.next;
       current.next = prev;
       prev = current;
       current = next;
    }

    return prev;
}


const node = reverse(head);
console.log(node);