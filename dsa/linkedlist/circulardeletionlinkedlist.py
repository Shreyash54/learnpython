class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class CLL:
  def __init__(self):
    self.head=None

  def insert(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      new_node.next=self.head
    else:
      current=self.head
      while current.next!=self.head:
        current=current.next
      current.next=new_node
      new_node.next=self.head
      self.head=new_node

  def deletefirst(self):
    if self.head is None:
      return
    current=self.head 
    while current.next !=self.head:
      current=current.next
    current.next=self.head.next
    self.head=self.head.next

  def delete_end(self):
    current=self.head
    if self.head is None:
      return
    if self.head.next==self.head:
      self.head=None

    else:
      while current.next.next!=self.head:
        current=current.next
      current.next=self.head
      
  def index(self,pos):
    if pos==0:
      return self.deletefirst()

    current=self.head
    if current.next==self.head:
      print("index out of rannge")
      return
      
    else:
      current=self.head
      count=0
      while current.next != self.head and count<pos-1:
        current=current.next
        count +=1
        if current.next == self.head:
                print("Index out of range")
                return

      current.next = current.next.next
     
  def search(self, key):
    if not self.head:
        print("List is empty")
        return None

    current = self.head
    while True:
        if current.data == key:
            return current
        current = current.next
        if current == self.head:
            break

    print(f"Key {key} not found in the list")
    return None

  
  def prin(self):
    current=self.head
    while  True:
      print(current.data,end="-->")
      current=current.next
      if current==self.head:
         break
    print()

my=CLL()
my.insert(4)
my.insert(46)
my.insert(445)
my.insert(56)
my.insert(40)
my.insert(235)
my.insert(85)
my.insert(65)
my.insert(65)
my.insert(15)
print("after inserions :")
my.prin()
print()
print("after deletions of first: ")
my.deletefirst()
my.prin()
print()

print("deletion at end:")
my.delete_end()
my.prin()
print()
print("deletion at index")
my.index(2)
my.prin()
print()
my.search(5)
my.prin()