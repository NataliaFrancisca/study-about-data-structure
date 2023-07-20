// const arr = [21,23,3,32,5];
// const arr = [3,5];
// const arr = [1,9,3,8,5];
// const arr = [1,2,3,4,5];
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

// FUNCTION TO REVERSE A LINKED LIST
function reverse_linked_list(list){
    let prev = null;

    while(list){
        let next = list.next;
        list.next = prev;
        prev = list;
        list = next;
    }

    return prev;
}

function reverse(head, left, right){
    let node_head = null;
    let node_tail = null;
    let node_left = null;
    let node_right = null;

    let index = 1;
    let current = head;

    while(current && index <= right){
        if(index < left){
            node_head = current;
        }

        if(index === left){
            node_left = current;
        }

        if(index === right){
            node_right = current;
            node_tail = current.next;
        }

        current = current.next;
        index++;
    }

    // quebrando o link entre o último nó dessa sublista e o tail
    node_right.next = null;
    node_right = reverse_linked_list(node_left);

    // verificando o head é null: então a lista esta revertendo a partir do head
    // verificando o head é true: então a lista não está sendo revertida a partir do head
    if(node_head){
        // então o next do head vai ser a sub lista que foi revertida
        node_head.next = node_right;
    }else{
        // então o head vai ser essa sub lista que foi revertida
        head = node_right;
    }

    // agora definindo que o node left => que é o último nó dessa sublista
    // seu next vai receber o tail
    node_left.next = node_tail;

    return head;
}

const node = reverse(head, 2, 4);

