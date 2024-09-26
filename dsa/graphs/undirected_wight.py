class graph:
  def __init__(self):
    self.graph={}
  def insertver(self,ver):
    if ver not in self.graph:
      self.graph[ver]={}
      print("vertex added")
  def insertedge(self,edg1,edg2,weights=None):
    if edg1 not in self.graph:
      self.insertver(edg1)
    if edg2 not in self.graph:
      self.insertver(edg2)

    self.graph[edg1][edg2]=weights
    self.graph[edg2][edg1]=weights
  def remove_ver(self,ver):
    if ver not in self.graph:
      print("vettex not found")
    else:
      for i in list(self.graph[ver]):
         del self.graph[i][ver]
      del self.graph[ver]
  def remove_edge(self,edg1,edg2):
    if edg1 and edg2 not in self.graph:
      print("vertex not found")
    else:
      if edg1 in self.graph and edg2 in self.graph[edg1]:
        del self.graph[edg1][edg2]
        del self.graph[edg2][edg1]
      print("edges removed")
  def display(self):
    for ver ,edg in self.graph.items():
      print(f"{ver}:{','.join(map(str,edg))}")
def main():
  g=graph()
  while True:
    print("enter the chocies")
    print("1. insert vertex")
    print("2. insert edges")
    print("3. rem ver")
    print("4. rem edges")
    print("5. display")
    print("6. exity")
    choice =input("enter tthe chocies")
    if choice=='1':
      ver=input("enet the vertex name")
      g.insertver(ver)
    if choice=='2':
      edg1=input("enter the edg1")
      edg2=input("enter the edg1")
      g.insertedge(edg1,edg2)
    if choice=='3':
      ver=input("enter the vertex name u wish to rmeove")
      g.remove_ver(ver)
    if choice=='4':
      edg1=input("enter the edg1")
      edg2=input("enter the edg2")
      g.remove_edge(edg1,edg2)
    if choice=='5':
      g.display()
    if choice=='6':
      print("exiting...")
      break

if __name__=="__main__":
  main()
    