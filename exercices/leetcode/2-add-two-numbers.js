// VALUES TO TEST THE FUNCTION
const arr_l1 = [2,4,3];
const arr_l2 = [5,6,4];

// THIS IS A VERSION THAT I DID USING LINKED LIST AND LISTNODE
class ListNode{
    constructor(value = 0, next = null){
        this.value = value;
        this.next = next;
    }
}

class LinkedList{
    constructor(head = null){
        this.head = head;
    }

    adicionar(value){
        let node = this.head;

        if(node == null){
            this.head = new ListNode(value);
            return;
        }

        while(node.next){
            node = node.next;
        }

        node.next = new ListNode(value);
    }

    print(){
        let currentNode = this.head;

        while(currentNode){
            console.log(currentNode.value);
            currentNode = currentNode.next;
        }

        return null;
    }
}

let l1 = new LinkedList();
let l2 = new LinkedList();

for(i in arr_l1){l1.adicionar(arr_l1[i])}
for(i in arr_l2){l2.adicionar(arr_l2[i])}

// VERSION USING LINKED LIST CLASS
function addTwoNumbers(l1, l2){
    let carry = 0;
    let l1_head = l1.head;
    let l2_head = l2.head;

    let linkedList = new LinkedList();

    while(l1_head || l2_head || carry){
        let value_1 = 0;
        let value_2 = 0;

        if(l1_head){
            value_1 = l1_head.value;
            l1_head = l1_head.next;
        }

        if(l2_head){
            value_2 = l2_head.value;
            l2_head = l2_head.next;
        }

        const sum = value_1 + value_2 + carry;
        const digit = sum % 10;

        carry = Math.floor(sum / 10);
        linkedList.adicionar(digit);
    }

    return linkedList;
}

console.log(addTwoNumbers(l1, l2));

// ---------------------------------------------------

// VERSION THAT I USE TO RESOLVE THE CODE ON THE LEETCODE PLATFORM
function addTwoNumbersI(l1, l2){
    let carry = 0;
    let l1_head = l1.head;
    let l2_head = l2.head;

    let linkedList = new ListNode();
    const headNode = linkedList;

    while(l1_head || l2_head || carry){
        let value_1 = 0;
        let value_2 = 0;

        if(l1_head){
            value_1 = l1_head.value;
            l1_head = l1_head.next;
        }

        if(l2_head){
            value_2 = l2_head.value;
            l2_head = l2_head.next;
        }

        const sum = value_1 + value_2 + carry;
        const digit = sum % 10;

        carry = Math.floor(sum / 10);
        const currentNode = new ListNode(digit);
        linkedList.next = currentNode;
        linkedList = currentNode;
    }

    return headNode.next;
}

console.log(addTwoNumbersI(l1, l2));