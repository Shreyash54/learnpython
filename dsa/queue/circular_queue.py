

class Queue:
  def __init__(self,size):
    self.size=size
    self.front,self.rear=-1,-1
    self.arr=[None]*size

  def enqueue(self,item):
    if self.is_full():
      raise IndexError("queue is full")
      
    if self.is_empty():
      self.front=0
      self.rear=0
    else:
      self.rear=(self.rear +1)%self.size
    self.arr[self.rear]=item

  def dequeue(self):
    if self.is_empty():
      raise IndexError("queu is empty")
    item=self.arr[self.front]
    if self.front==self.rear:
      self.front=-1
      self.rear=-1
    else:
      self.front=(self.front+1)%self.size
    return item

  def display(self):
    current=self.front
    array=[]
    while True:
      array.append(self.arr[current])
      if current==self.rear:
        break
      current=(current+1)%self.size
    return array
      

  def is_empty(self):
    return self.front==-1
  def is_full(self):
    return (self.rear+1)%self.size==self.front

c1=Queue(5)
c1.enqueue(5)
c1.enqueue(45)
c1.enqueue(45)
c1.enqueue(45)
c1.enqueue(45)
c1.dequeue()
c1.dequeue()
print(c1.display())