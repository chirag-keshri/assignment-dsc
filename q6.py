def decimalToBinary(n): 
  
    if n > 1: 
        decimalToBinary(n//2)  
    print (n%2)                 
   
if __name__ == '__main__': 
    decimalToBinary(12) 
    print