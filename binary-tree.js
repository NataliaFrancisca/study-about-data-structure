class Node{
    constructor(data){
        this.data = data;
        this.leftChild = null;
        this.rightChild = null;
    }

    append(value){

        if(value < this.data){
            if(this.leftChild){
                this.leftChild.append(value);
            }else{
                this.leftChild = new Node(value);
            }
            return;
        }else{
            if(this.rightChild){
                this.rightChild.append(value);
            }else{
                this.rightChild = new Node(value);
            }
            return
        }

    }


}


const mytree = new Node(12);
mytree.append(7);
mytree.append(14)
mytree.append(3);
mytree.append(8);
mytree.append(1);
console.log(mytree.leftChild)