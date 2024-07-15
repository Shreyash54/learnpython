class A:
  def __init__(self,name):
    self.name=name

class dog(A):
  def speaks(self):
    return f"we are {self.name}"
class cat(A):
  def speaks(self):
    return f"df cerw {self.name}"

obj1=dog("maher")
obj2=cat("df")
print(obj1.speaks())
print(obj2.speaks())

class Base: 
  def __init__(self): 
      self.a = "GeeksforGeeks"
      self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
  def __init__(self): 

      # Calling constructor of 
      # Base class 
      Base.__init__(self) 
      print("Calling private member of base class: ") 
      print(self.__c) 


# Driver code 
obj1 = Base() 
print(obj1.a) 
print(obj1.__c) 
# raise an AttributeError





