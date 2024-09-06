class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1

class AVL:
  def __init__(self):
      self.root = None

  def get_height(self, node):
      return node.height if node else 0

  def get_balance(self, node):
      return self.get_height(node.left) - self.get_height(node.right) if node else 0

  def right_rotate(self, y):
      x = y.left
      t2 = x.right

      # Perform rotation
      x.right = y
      y.left = t2

      # Update heights
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
      x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

      # Return new root
      return x

  def left_rotate(self, x):
      y = x.right
      t2 = y.left

      # Perform rotation
      y.left = x
      x.right = t2

      # Update heights
      x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

      # Return new root
      return y

  def insert(self, root, data):
      if not root:
          return Node(data)
      elif data < root.data:
          root.left = self.insert(root.left, data)
      elif data > root.data:
          root.right = self.insert(root.right, data)
      else:
          # Duplicate data is not allowed
          return root

      # Update height of this ancestor node
      root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

      # Get the balance factor of this ancestor node
      balance = self.get_balance(root)

      # Balancing the node if it becomes unbalanced

      # Left Left Case
      if balance > 1 and data < root.left.data:
          return self.right_rotate(root)

      # Right Right Case
      if balance < -1 and data > root.right.data:
          return self.left_rotate(root)

      # Left Right Case
      if balance > 1 and data > root.left.data:
          root.left = self.left_rotate(root.left)
          return self.right_rotate(root)

      # Right Left Case
      if balance < -1 and data < root.right.data:
          root.right = self.right_rotate(root.right)
          return self.left_rotate(root)

      # Return the (unchanged) node pointer
      return root

  def in_order(self, root):
      arr = []
      if root:
          arr = self.in_order(root.left)
          arr.append(root.data)
          arr = arr + self.in_order(root.right)
      return arr

# Example usage
avl = AVL()
root = None

# Insert elements
keys = [10, 20, 30, 15]
for data in keys:
  root = avl.insert(root, data)

# Print in-order traversal
print("In-order traversal:", avl.in_order(root))
