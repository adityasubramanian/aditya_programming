 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node Insert(Node root,int value) {
        if (root == null) {
            Node temp = new Node(); 
            temp.data = value; 
            root = temp; 
        }
        if (root.data > value) {        // Left side of the tree. 
              root.left = Node.Insert(root.left,value);
        }
        if (root.data < value) {        // Right side of the tree. 
            root.right = Node.Insert(root.right,value); 
        }
       return root; 
} 

