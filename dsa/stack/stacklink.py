class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class stack:
  def __init__(self):
    self.top=None
    self._size=0

  def push(self,data):
    new_node=Node(data)
    if self.top is None:
      self.top =new_node
    else:
      new_node.next=self.top
      self.top=new_node
      self._size +=1

  def pop(self):
    current=self.top
    if self.top is None:
      return self.is_empty()
    else:
      self.top=current.next
      self._size-=1

  def is_empty(self):
    return self.top is None

  def size(self):
    current=self.top
    arr=[]
    while current:
      arr.append(current.data)
      current=current.next
    return len(arr)
      

  def display(self):
    current=self.top
    while current:
      print(current.data,end="-->")
      current=current.next
  
s=stack()
s.push(45)
s.push(45)
s.push(75)
s.push(65)
s.push(545)
s.push(5)
s.push(4)
s.pop()
s.display()
print(s.is_empty())
print(s.size())
s.display()