import os 


def create_file(filename):
  try:
    with open(filename,'w') as f:
      f.write("orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose")
      print("file is sucessfullt crated")
  except IOError:
    print (f"there is wrroe in creation {filename} ")


def delete_file(filename):
  try:
    os.remove(filename)
    print("thwe file is deleted",filename)
  except IOError:
    print("ther is eroor in deleetion",filename)

def read_file(filename):
  try:
    with open(filename ,'r') as f:
     # contents =f.read(3)
      contents =f.readlines()
      print("the contents are {}".format(contents))
  except IOError:
    print("there is error in reading {}".format(filename))



def append_to_file(filename):
  try: 
    with open(filename,'a') as f:
      f.write("sc ercer erfer rwfe rf")
      print("appended succesfully")
  except IOError:
    print("ther is wrong in error")


def rename(filename,newname):
  try:
    os.rename(filename,newname)
    print("rename succesfully {}".format(newname))
  except IOError:
    print("ther is error in renaming")


if __name__=="__main__":
  filename="lex.txt"
  newname ="new_name.txt"
  create_file(filename)
  read_file(filename)
  append_to_file(filename)
  rename(filename,newname)
  #delete_file(filename)
  #delete_file(newname)
