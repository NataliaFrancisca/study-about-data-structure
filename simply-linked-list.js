class Node{
    constructor(value = null, next = null){
        this.value = value;
        this.next = next;
    }
}

class LinkedList{
    constructor(head = null){
        this.head = head;
    }

    append(value){
        let node = this.head;

        if(this.head == null){
            this.head = new Node(value);
            return;
        }

        while(node.next){
            node = node.next
        }

        node.next = new Node(value);
    }

    remove(node){
        let prevNode = null;
        let currentNode = this.head;
   
        while(currentNode){
            let nextNode = currentNode.next;

            if(currentNode.value === node){
                if(prevNode === null){
                    this.head = nextNode;
                    prevNode = null;
                }else{
                    prevNode.next = currentNode.next;
                }
            }else{
                prevNode = currentNode;
            }

            currentNode = nextNode;                
        }

        return null;
    }

    print(){
        let currentNode = this.head;

        while(currentNode){
            console.log("NODE", currentNode.value);
            currentNode = currentNode.next;
        }

        return null;
    }
}

const list_1 = new LinkedList();

// [1,2,2,1]

list_1.append(7);
list_1.append(7);
list_1.append(7);
list_1.append(7);

// list_1.print();

list_1.remove(7);


list_1.print();