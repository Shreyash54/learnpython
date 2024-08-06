class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class queue:
  def __init__(self):
    self.front=None
    self.rear=None
    self._size=0
  def enqueue(self,data):
    new_node=Node(data)
    if self.front is None:
      self.front=self.rear=new_node
    else:
      self.rear.next=new_node
      self.rear=new_node
    self._size+=1

  def dequeue(self):
    if self.front is None:
      raise IndexError("empty queue add something")
    else:
      self.front=self.front.next
    self._size-=1

  def display(self):
    current=self.front
    while current:
      print(current.data,end="-->")
      current=current.next
    print(None)
    
  def size(self):
    return self._size
q=queue()
q.enqueue(45)
q.enqueue(989)
q.enqueue(87)
q.enqueue(65)
q.enqueue(5)
q.dequeue()
q.display()
print(q.size())