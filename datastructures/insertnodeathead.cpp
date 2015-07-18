/*
  Insert Node at the begining of a linked list
  Initially head pointer argument could be NULL for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
return back the pointer to the head of the linked list in the below method.
*/
struct Node {
  int data; 
  struct Node *next; 
}; 


Node* Insert(Node *head,int data)
{
  Node* current = new Node; 
  current -> data = data; 

  if (current -> next != NULL) {
  	current -> next = NULL; 
  }

  if (head == NULL) {
  	head == current; 
  } else {
  	if (head != NULL) {
  		current -> next = head; 
  		head = current; 
  	} 
  }
  return head; 
}



