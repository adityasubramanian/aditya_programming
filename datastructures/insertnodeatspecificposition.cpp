  struct Node
  {
     int data;
     struct Node *next;
     struct Node *prev; 
  }
Node* InsertNth(Node *head, Node *tail, int data, int position) {
    Node* temp = new Node(data); 
    temp -> data = data;        
    temp -> next = NULL;
    temp -> prev = tail; 
    Node* temp2 = head;
    if (position == 0) {
      temp -> next = head; 
      head = temp; 
      temp = NULL;      
    } else {
        for (int currentposition = 1 ; currentposition < position; currentposition++) 
            temp2 = temp2 -> next; 
            temp -> next = temp2 -> next; 
            temp2 -> next = temp; 
    }
    return head; 
}
