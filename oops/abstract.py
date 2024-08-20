from abc import ABC ,abstractmethod


class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class rectangle(Shape):
  def __init__(self,width,length):
    self.width=width
    self.length=length


  def area(self):
    return self.width*self.length

  def perimeter(self):
    return self.length+self.width

class circle(Shape):

  def __init__(self, radius):
      self.radius = radius

  def area(self):
      import math
      return math.pi * (self.radius ** 2)

  def perimeter(self):
      import math
      return 2 * math.pi * self.radius


rect=rectangle(10,10)

cir=circle(3)
print(f"rectange area is {rect.area()} and perimeter is {rect.perimeter()}")


print("area is{}".format(cir.perimeter()))


class emp: 
  def __init__(self): 
      self.name = 'xyz'
      self.salary = 4000

  def show(self): 
      print(self.name) 
      print(self.salary) 

e1 = emp() 
print("Dictionary form :", vars(e1)) 
print(dir(e1)) 


#vars to find class atrribute
#dir to find more about class attribute
