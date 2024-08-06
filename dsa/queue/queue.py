


class Queue:
  def __init__(self):
    self.arr=[]

  def queue(self,item):
      self.arr.append(item)

  def is_empty(self):
    if len(self.arr)==0:
      return True
  def dequeu(self):
    if self.is_empty():
      return IndexError("deuqu form empty arr")
    else:
      self.arr.pop(0)

  def size(self):
    return len(self.arr)

  def display(self):
    print(self.arr)

q=Queue()
q.queue(45)
q.queue(5)
q.queue(4)
q.display()
q.dequeu()
q.display()
print(q.is_empty())