"""transpose using plain python 
      zip with List comprehension"""

matrix=[[10,20,30],
        [40,50,60],
       [70,80,90]]
mat=[]
lis=[list(row) for row in zip(*matrix)]
print(lis)
