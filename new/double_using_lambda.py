def double(num):
  if num%2==0 and 1:
    return num*2
  else:
    return num

num =[2,35,35]
print(list(map(lambda num: num * 2, num)))




name =['erf','erf','erf','rqwf']
age=[34,324,53,66]
for i ,(nam,ag) in enumerate(zip(name,age)):
  print(nam,ag)



stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = dict(zip(stocks, prices))
print(new_dict)

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
re = list(zip(tuple1, tuple2))
#result = list(zipped)

print(re,ord('$'))
