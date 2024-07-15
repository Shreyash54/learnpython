def printsolution(board):
  for row in board:
    print(" ".join(map(str,row)))
    print("\n")
  
def is_safe(board,row,col,n):
  for i in range(n):
    if board[i][col]==1:
      return False

  for j in range(n):
    if board[row][j]==1:
      return False

  i,j=row,col
  while i>=0 and j>=0:
      if board[i][j]==1:
        return False
      i,j = i-1 , j-1

  i,j =row,col
  while i>=0 and j<n:
    if board[i][j]==1:
      return False
    i,j= i-1,j+1

  return True

def Nqueensuntil(board,row,n):
  if row == n:
    printsolution(board)
    return True
    
  for col in range(n):
    if is_safe(board,row,col,n):
         board[row][col]=1
         Nqueensuntil(board,row+1,n)
         board[row][col]=0
    

def Nqueens():
  n=int(input("enter no of queens to back track:"))
  board =[[0]*n for _ in range(n)]
  Nqueensuntil(board,0,n)


Nqueens()