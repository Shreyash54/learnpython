class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class Link:
  def __init__(self):
    self.head=None

  def insert(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node

  def delbegin(self):
    if self.head is None:
      print("empty")
      return None
    else:
      self.head=self.head.next


  def del_end(self):
    current=self.head
    if self.head is None:
      print("List is empty")
      return
    while current.next.next is not None:
      current=current.next
    current.next=None
    
  def delatpos(self,pos):
    if pos==0:
      self.delbegin()
      return print("done")
    if self.head is None:
      print("list is empty")
      return
    current=self.head
    count=0
    while current.next is not None and count<pos-1:
      current=current.next
      count+=1
    current.next=current.next.next
      
  def delete_by_value(self, value):
    if self.head is None:
        print("List is empty")
        return

    # Case where the node to be deleted is the head
    if self.head.data == value:
        self.head = self.head.next
        return

    current = self.head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            return
        current = current.next
      
  def print_list(self):
    current = self.head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

  def search(self,value):
    current=self.head
    while current is not None:
      if current.data==value:
        print("found in the list")
        return True
      current=current.next
    print("not found")
    return False
      
  # Example usage:
my_list = Link()

  # Inserting nodes at the beginning
my_list.insert(3)
my_list.insert(2)
my_list.insert(29)
my_list.insert(5)
my_list.insert(155)

print("Initial linked list:")
my_list.print_list()

  # Deleting from beginning
#my_list.del_end()
#print("Linked list after deleting from beginning")
#my_list.delete_by_value(2)
#my_list.delete_by_value(29)

#my_list.delatpos(1)
#my_list.delatpos(0)
#my_list.print_list()
my_list.search(2)



      
    
    
      
      
