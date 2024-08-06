

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LL:
  def __init__(self):
    self.head=None

  def insert(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      new_node.next=self.head
    else:
      temp=self.head
      while temp.next !=self.head:
        temp=temp.next
      temp.next=new_node
      new_node.next=self.head
      self.head=new_node
      
  def insert_end(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
    else:
      current=self.head
      while current.next !=self.head:
        current=current.next
      current.next=new_node
      new_node.next=self.head
        

  def display(self):
    if self.head is None:
        print("List is empty.")
        return
    temp = self.head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == self.head:
            break
    print()

  def inser_at_pos(self,data,pos):
    new_node=Node(data)
    if self.head is None:
      self.head =new_node
      new_node.next=self.head
    if pos<0:
      print("Invalid position insertiosn")
    else:
      current=self.head
      count=0
      while current:
        if count==pos-1:
          new_node.next=current.next
          current.next=new_node
          return
        current=current.next
        count +=1
        if current == self.head:  # Reached back to head without finding pos-1
                print("Position out of bounds")
                return
        print("Position out of bounds")
          
    
  def search(self, value):
    if self.head is None:
        print("List is empty.")
        return -1  # Return -1 indicating value not found

    temp = self.head
    pos = 0
    while True:
        if temp.data == value:
            return pos  # Return the position if value is found
        temp = temp.next
        pos += 1
        if temp == self.head:
            break

    print(f"Value {value} not found in the list.")
    return -1  # Return


list=LL()

list.insert(1)
list.insert(121)
list.insert(149)
list.insert(154)
list.insert(14)
list.insert_end(3)
list.display()
list.inser_at_pos(45,4)
list.display()
list.search(45)
