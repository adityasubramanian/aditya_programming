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
public Node rightNode() {
	return right; 
}

void Postorder(Node root) {
	if (root != null) {
		Postorder(root.leftNode());
		Postorder(root.righgtNode()); 
		System.out.print(root.data, " "); 
	}
	return; 
}

