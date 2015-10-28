/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/
public Node leftNode() {
    return left; 
}
public Node rightNode(){ 
    return right; 
}
void Preorder(Node root) {
    if (root != null) {
        System.out.print(root.data + " "); 
        Preorder(root.leftNode()); 
        Preorder(root.rightNode());     
    }
    return; 
}
