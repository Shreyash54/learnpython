class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BT:
  def __init__(self):
    self.root=None
  def insert(self,data):
    new_node=Node(data)
    if self.root is None:
      self.root=new_node
    else:
      self._insert(self.root,new_node)
      
  def _insert(self,root,new_node):
    if new_node.data<root.data:
      if root.left is None:
        root.left=new_node
      else:
        self._insert(root.left,new_node)
    elif new_node.data>root.data:
      if root.right is None:
        root.right =new_node
      else:
        self._insert(root.right,new_node)
      
    
  def delete(self,data):
    self.root=self._delete(self.root,data)
  def _delete(self,root,data):
    if root is None:
      return root
    if data<root.data:
      root.left=self._delete(root.left,data)
    elif data>root.data:
      root.right=self._delete(root.right,data)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      successor=self.find_min(root.right)
      root.data=successor.data
      root.right=self._delete(root.right,successor.data)



  def find_min(self,root):
    current=root
    while current.left is not None:
      current=current.left
    return current
  def inorder(self):
    arr=[]
    self._inorder(self.root,arr)
    return arr
  def _inorder(self,root,arr):
    if root:
      self._inorder(root.right,arr)
      arr.append(root.data)
      self._inorder(root.left,arr)

  def height(self):
    return self._height(self.root)
  def _height(self,root):
    if root is None:
      return 0
    else:
      return 1+max(self._height(root.left),self._height(root.right))


  def depth(self,data):
    return self._depth(self.root,data,0)
  def _depth(self,root,data,curr_depth):
    if root is None:
      return -1
    else:
      if root.data==data:
        return curr_depth
      elif data<root.data:
        return self._depth(root.left,data,curr_depth+1)
      else:
        return self._depth(root.right,data,curr_depth+1)
    

bt = BT()

# Insert elements
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)
print("height is bst is :" ,bt.height())

# In-order traversal
print("In-order Traversal:", bt.inorder())   # Output: [20, 30, 40, 50, 60, 70, 80]
print("depth is :",bt.depth(20))