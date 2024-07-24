def deco(cls):
  def wrapper():
    print("hello before \n")
    cls()
    print("hello afer \n")
  return wrapper

@deco
def say_hello():
    print("Hello! \n"*5)
say_hello()




#to add subrtact
def decorate(func):
  def wrapper(*args,**kwargs):
    print(f"the result is {func.__name__} with args")
    return func(*args,**kwargs)
  return wrapper
  __
  
@decorate
def add(a,b):
  return a+b
@decorate
def multiply(a,b):
  return a*b
print(f" additipn is {add(5,6)} \n" )
print(f"anser is {multiply(4,5)} \n")

# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(f"the factorial is {math.factorial(num)} \n")

# calling the function.
factorial(10)


class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def insert_at_beginning(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.data, end=" -> ")
          current_node = current_node.next
      print("None")

# Example usage:
llist = LinkedList()
llist.insert_at_beginning("C")
llist.insert_at_beginning("B")
llist.insert_at_beginning("A")
llist.print_list()