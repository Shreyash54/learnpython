
#generator
def generator():
  for i in range(5):
    yield i

gen= generator()
for j in gen:
  print(j)

#function caaching


from functools import lru_cache

@lru_cache(maxsize=None)
def fun(n):
  import time
  time.sleep(5)
  return n*5

print(fun(10))
print("doen for 10")
print(fun(5))
print("done for 5")
print(fun(10))
print("donw for 10")
print(fun(5))
print("done for 5")

  