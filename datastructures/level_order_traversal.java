   /* 
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   void LevelOrder(Node root)
    {
		Queue<Node> queue = new LinkedList<Node>(); // Initializes a queue based linked list. 
		queue.add(root); 									
		while (!queue.isEmpty()) {
			Node temp = queue.poll(); 
			System.out.print(temp.data + " "); 
			if (temp.left != null) {
				queue.add(temp.left); 
			}
			if (temp.right != null) {
				queue.add(temp.right); 
			}
		}      
      
    }
