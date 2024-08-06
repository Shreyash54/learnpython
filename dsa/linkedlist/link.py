class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class link:
  def __init__(self):
    self.head=None

  def insertatbegin(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node

  def insertatend(self,data):
    current=self.head
    new_node=Node(data)

    if self.head is None:
     self.head=new_node
     return

    while current.next is not None:
      current=current.next
  
    current.next=new_node

  def insertatpos(self,pos,data):
    new_node=Node(data)
    if pos==0:
      self.insertatbegin(data)
      return

    current=self.head
    count=0
    
    while current is not None and count<pos-1:
      current=current.next
      count+=1
    if current is None:
      print("postion out of bound")
    else:
      new_node.next=current.next
      current.next=new_node
  
  def print(self):
    current=self.head
    while current:
      print(current.data, end="-->")
      current=current.next
    print("None")

my=link()
my.insertatbegin(2)
my.insertatbegin(5)
my.insertatbegin(6)
my.insertatbegin(7)
my.insertatend(1)
my.insertatpos(3,88)
my.print()