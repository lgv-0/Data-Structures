"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        self.head.delete()
        old_value = self.head.value
        if (self.head.prev):
            self.head = self.head.prev
        elif (self.head.next):
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        self.length -= 1

        return old_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        self.tail.delete()
        old_value = self.tail.value
        if (self.tail.prev):
            self.tail = self.tail.prev
        elif (self.tail.next):
            self.tail = self.tail.next
        else:
            self.head = None
            self.tail = None

        self.length -= 1

        return old_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if (self.tail is node):
            self.tail = self.tail.prev

        node.delete()
        self.head.prev = node
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if (self.head is node):
            self.head = self.head.next

        node.delete()
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        node.delete()
        if (node is self.head and node is self.tail):
            self.head = None
            self.tail = None
        if (node is self.head):
            self.head = node.next
        elif (node is self.tail):
            self.tail = node.prev
        
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        val = self.head.value

        while (current):
            if val < current.value:
                val = current.value
            
            current = current.next

        return val