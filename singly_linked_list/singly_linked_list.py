class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        
        self.length += 1

    def remove_head(self):
        if self.head:
            self.length -= 1
            if (self.tail is self.head):
                ref_value = self.head.value
                self.tail = None
                self.head = None
                return ref_value
            else:
                ref_value = self.head.value
                self.head = self.head.next_node
                return ref_value

    def remove_tail(self):
        if (self.tail is None):
            return None

        if (self.tail is self.head):
                ref_value = self.head.value
                self.tail = None
                self.head = None
                self.length -= 1
                return ref_value

        current = self.head
        last = None

        while True:
            if self.tail is current:
                val = self.tail.value
                self.tail = last
                self.length -= 1
                return val
            else:
                last = current
                current = current.next_node

    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head

        while current:
            if current.value is value:
                return True
            
            current = current.next_node

        return False

    def print_list(self):
        if self.head is not None:
            current = self.head
            while True:
                print(current.value)

                if (current.next_node is None):
                    break

                current = current.next_node
    
    def get_max(self):
        if not self.head:
            return None

        highestvalue = self.head.value

        current = self.head

        while current:
            if current.value > highestvalue:
                highestvalue = current.value

            current = current.next_node
        
        return highestvalue

    def __len__(self):
        return self.length