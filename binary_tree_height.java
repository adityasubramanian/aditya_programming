   /*
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   int height(Node root) {
       if (root != null) {
           return (Math.max(height(root.left)+1,height(root.right)+1)); 
       }
       return 0;       
   }
