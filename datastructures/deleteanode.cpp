struct Node {
  int data;
  struct Node *next;
}; 
Node* Delete(Node* head, int position) {
      Node* temp_head;    
      temp_head = head;    
      if (position == 0) {      
          head = head -> next;  
          delete temp_head;    
          temp_head = NULL;     
      } else {
        for (int i = 1 ; i < position; i++) {
            temp_head  = temp_head -> next; 
        }
         temp_head -> next = (temp_head -> next) -> next; 
      } 
      return head; 
}
