/* you only have to complete the function given below.  
Node is defined as  

class Node {
    int data;
    Node left;
    Node right;
}

*/
public Node rightNode(){
    return right; 
}
public Node leftNode() {
    return left; 
}
void Inorder(Node root) {
    if (root != null) {
        Inorder(root.leftNode()); 
        System.out.print(root.data + " "); 
        Inorder(root.rightNode());        
    }
    return; 
}
