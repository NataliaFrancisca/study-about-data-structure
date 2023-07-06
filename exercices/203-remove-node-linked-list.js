let head = null;
const val = 6;

class ListNode{
    constructor(value = 0, counter = 0, next = null){
        this.value = value;
        this.counter = counter;
        this.next = next;
    }
}

function initialize(value, counter){
    let node = head;

    if(node == null){
        head = new ListNode(value, counter);
        return;
    }

    while(node.next){
        node = node.next;
    }

    node.next = new ListNode(value, counter);
}

var removeElements = function(head, val) {
    let prevNode = null;
    let currentNode = head;

    while(currentNode){
        let nextNode = currentNode.next;

        if(currentNode.value === val && prevNode === null){
            head = nextNode;
            prevNode = null
        }

        if(currentNode.value === val && prevNode){
            prevNode.next = currentNode.next;
        }

        if(currentNode.value !== val){
            prevNode = currentNode;
        }

        currentNode = nextNode;
    }

    return head;
};


// const arr = [1,2,6,3,4,5,6];
const arr = [7,7,7,7];

for(let i = 0; i < arr.length; i++){
    initialize(arr[i], i);
}

const node = removeElements(head, 7);
console.log(node)