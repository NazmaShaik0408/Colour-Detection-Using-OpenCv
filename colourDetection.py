class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Singly_linked_list:
    def __init__(self):
        self.head=None

    def add_at_front(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode

    def add_at_middle(self,data,pos):
        if pos<0:
            return
        if self.head==None:
            self.head=Node(data)
        else:
            safe=self.head
            while pos-1>0:
                safe=safe.next
                pos-=1
            newnode=Node(data)
            newnode.next=safe.next
            safe.next=newnode
        
    def add_at_last(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            safe=self.head
            while safe.next!=None:
                safe=safe.next
            safe.next=Node(data)

    def display(self):
        safe=self.head
        while safe!=None:
            print(safe.data,end='->')
            safe=safe.next
        print("None")

    def length_iteration(self):
        current=self.head
        count=0
        while current!=None:
            current=current.next
            count+=1
        return count
    
    def length_recursion(self):
        return self.__length_recursion_helper(self.head)
    
    def __length_recursion_helper(self,node):
        if node==None:
            return 0
        return 1+self.__length_recursion_helper(node.next)

sll=Singly_linked_list()
sll.add_at_front(19)
sll.add_at_front(27)
sll.add_at_last(32)
sll.add_at_last(52)
sll.add_at_middle(48,2)
sll.add_at_middle(76,3)
sll.display()
print(sll.length_recursion())