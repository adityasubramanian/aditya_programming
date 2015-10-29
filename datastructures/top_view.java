/*
   class Node 
       int data;
       Node left;
       Node right;
*/
public void left(Node lroot) {
    if (lroot != null) {
        left(lroot.left); 
        System.out.print(lroot.data + " "); 
    }
    return; 
}
public void right(Node rroot) {
    if (rroot != null) {
        System.out.print(rroot.data + " "); 
        right(rroot.right); 
    }
    return; 
}
void top_view(Node root)
{
  if (root != null) {
      left(root.left); 
      System.out.print(root.data + " "); 
      right(root.right);
   }
}