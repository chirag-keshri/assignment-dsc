n=int(input("enter rows:"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
      if row==col:
        print((2*row)-1)
      elif col==1: 
        print((2*row)-row,end=" ")
      elif row>col:
          print((row+col)-1,end=" ")
     
    print()