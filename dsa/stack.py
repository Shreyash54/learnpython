class stack:
  def __init__(self):
    self.items=[]

  def push(self,item):
    self.items.append(item)

  def pop(self):
    if self.is_empty():
      raise IndexError("empty stack")
    return self.items.pop()

  def peek(self):
    if self.is_empty():
      raise IndexError("peek empty stak")
    return self.items[-1]

  def is_empty(self):
    return len(self.items)==0

  def size(self):
    return len(self.items)

  def prin(self):
    print(self.items)

s=stack()
s.push(56)
s.push(56)
s.push(56)
s.push(56)
s.pop()
print(s.peek())
s.prin()
print(s.is_empty())
