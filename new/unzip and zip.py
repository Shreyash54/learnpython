"""""the zip() function is used to combine two or more lists (or any other iterables) into a single iterable, where elements from corresponding positions are paired together. The resulting iterable contains tuples, where the first element from each list is paired together, the second element from each list is paired together, and so on.""""""
"""""
""""
Unzipping Using zip()
Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator.
"""""



name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)



###########################################################
stocks =['cerf','fewrf']
prices=[134,34]
dic =list(zip(stocks,prices))
print(dic)

soccer=["we","eqrf"]
player=[3,434]
for i ,(soc ,pal) in enumerate(zip(soccer,player)):
  print(i,soc ,pal)

############################################################
def split(inputstr,param=" "):
  pair=[inputstr[i:i+2] for i in range(0,len(inputstr),2)]
  return pair

inputstr=input("enter the string:")
spl=split(inputstr,",")

for pir in spl:
  if len(pir) == 2:
      print(f"ASCII value of '{pir}' is {ord(pir[0])} {ord(pir[1])}")
    #######################################################