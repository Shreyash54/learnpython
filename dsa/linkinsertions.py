class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class linkedlist(Node):
  def __init__(self):

    self.head=None

  def insert_at_begin(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next is not None:
      current = current.next

    current.next = new_node

  def in_at_pos(self, pos, data):
    new_node = Node(data)

    if pos == 0:
        self.insert_at_begin(data)
        return

    current = self.head
    count = 0

    while current is not None and count < pos - 1:
        current = current.next
        count += 1

    if current is None:
        print("Position is out of bounds.")
    else:
        new_node.next = current.next
        current.next = new_node



def prints(head):
  current=head
  while current:
    print(current.data, end="-- -> ")
    current=current.next

  print(None)


my_list = linkedlist()

# Insert nodes at the beginning
my_list.insert_at_begin(3)

my_list.insert_at_begin(2)
my_list.insert_at_begin(1)
my_list.insert_at_end(5)
my_list.in_at_pos(4,55)
prints(my_list.head)