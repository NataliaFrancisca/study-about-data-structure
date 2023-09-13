let head = null;

class ListNode{
    constructor(value = 0, next = null){
        this.value = value;
        this.next = next;
    }
}

var removeElements = function(head, val) {
    let prevNode = null;
    let currentNode = head;

    while(currentNode){
        let nextNode = currentNode.next;

        if(currentNode.value === val){
            if(prevNode === null){
                head = nextNode;
                prevNode = null;
            }else{
                prevNode.next = currentNode.next;
            }
        }else{
            prevNode = currentNode;
        }

        currentNode = nextNode;
    }

    return head;
};

// FUNCTION TO ADD THE NUMBERS AS A NODE 
function initialize(value){
    let node = head;

    if(node == null){
        head = new ListNode(value);
        return;
    }

    while(node.next){
        node = node.next;
    }

    node.next = new ListNode(value);
}

// NODE LIST TEST
const arr = [1,2,6,3,4,5,6];
// const arr = [7,7,7,7];

for(let i = 0; i < arr.length; i++){
    initialize(arr[i]);
}

const node = removeElements(head, 6);
console.log(node)