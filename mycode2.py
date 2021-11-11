# This is the example of print simple pyramid pattern  
n = int(input("Enter the number of rows"))  
# outer loop to handle number of rows  
for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print()  

        
        # This is the example of print simple reversed right angle pyramid pattern  
rows = int(input("Enter the number of rows:"))  
k = 2 * rows - 2  # It is used for number of spaces  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")  
