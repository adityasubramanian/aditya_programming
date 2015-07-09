/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
struct Node {
     int data;
     struct Node *next;
}; 

Node* Insert(Node *head,int data)
{
 	Node* current = new Node; 
 	current-> data = data; 
 	if (current -> next != NULL) {
 		current -> next = NULL; 
 	}
 	if (head == NULL) {
 		head = current; // No more elements in the linked list. 
 	} else if (head!=NULL){
 		Node *secondaryhead = new Node; 
 		secondaryhead = head; 
 		while (secondaryhead -> next != NULL) {
 			secondaryhead = secondaryhead -> next; 	// Traverses until meeting the end of the linked list.  
 		}
 		secondaryhead -> next = current; // Places the Node at the ned of the linked list. 
 	}
 	return head; // Returns the linked list. 
}
