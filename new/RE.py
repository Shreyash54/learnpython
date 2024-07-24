import re
text="fqerf erf34$$$rf rr3f3r"
f1 =re.findall('er',text)
print(f1)


# Original matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

matrix=[]

for i in range(len(twoDMatrix[0])):
  new_row=[]
  for row in twoDMatrix:
    new_row.append(row[i])
    matrix.append(new_row)


for row in twoDMatrix:
  print(row)