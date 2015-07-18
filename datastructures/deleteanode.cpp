struct Node {
  int data;
  struct Node *next;
}; 

Node* Delete(Node* head, int position) {
  Node* temp_head = head; 
  if (position == 0) {
    head = head -> next; 
    delete temp_head; 
    temp_head = NULL;
  } else {
    int counter = 0; 
    if (temp_head != NULL &&  ((counter+1) != position)) {
      temp_head = temp_head -> next; 
      counter++;
      if ((counter+1 == position)){
        temp_head -> next = (temp_head -> next) -> next; 
     } 
    } 
  }
  return head; 
}




