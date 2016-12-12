class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist(self):
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def inserafterprev(self,prev_node,new_data):
        if (prev_node == None):
            print "GET LOST U FOOL!!"
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def inseratend(self,new_data):
        new_node = Node(new_data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp  = temp.next
        temp.next = new_node

list = Linkedlist()
list.head = Node(2)
sec = Node(5)
thr = Node(9)
list.head.next = sec
sec.next = thr
