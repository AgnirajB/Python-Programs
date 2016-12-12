class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def remove(self,key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
    def removepos(self,pos):
        temp = self.head
        if (temp is not None):
            if (temp == )
        for i in range(pos):

    def prilist(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next



list = Linkedlist()
list.head = Node(2)
sec = Node(5)
thr = Node(9)
list.head.next = sec
sec.next = thr
list.remove(5)
list.prilist()
