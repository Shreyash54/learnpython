class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

class DLL:
  def __init__(self):
    self.head=None

  def insert(self,data):
    new_node= Node(data)
    if self.head is None:
      self.head=new_node
      return
    else:
      new_node.next=self.head
      self.head.prev=new_node
      self.head=new_node
      
  def insertend(self ,data):
    new_node = Node(data)
    if self.head is None:
      self.insert(data)
      return
    else:
      current=self.head
      while current.next is not None:
        current=current.next
      new_node.prev=current
      current.next=new_node
        
  def display(self):
    current=self.head
    while current is not None:
      print(current.data,end="-->")
      current=current.next
    print(None)


  def insertpos(self,pos,data):
    if pos==0:
      self.insert(data)
      return
    else:
      new_node=Node(data)
      current=self.head
    for i in range(0,pos-1):
      current=current.next
    new_node.next=current.next
    new_node.prev=current
    current.next.prev=new_node
    current.next=new_node


  
  def delpos(self,pos):
    current=self.head
    if current is None:
      self.del_beg(data)
      return
    if current.next is None:
      self.deleteend(data)
      return
      
    count=0
    while current is not None and count<pos:
      current=current.next
      count+=1
    # Node to be deleted is in the middle
    current.next.prev=current.prev
    current.prev.next=current.next
    


  def del_beg(self):
    if self.head is None:
      print("lsit empty")
      return
    else:
      self.head=self.head.next
      self.head.prev=None

  def deleteend(self):
    current=self.head
    while current.next is not None:
      current=current.next
    current.prev.next=None


  def display_back(self):
    node=[]
    temp=self.head
    while temp:
      node.append(temp.data)
      temp=temp.next
    reversed=node[::-1]
    for i in reversed:
      print(i,end="<-->")
    print()
    
list=DLL()
list.insert(45)
list.insert(12)
list.insert(87)
list.insert(56)
list.insert(23)
list.insertend(69)
list.insertend(69)
list.insertpos(5,4)
list.display()
list.del_beg()
#list.deleteend()
#list.deleteend()
list.delpos(3)
list.display()
list.display_back()