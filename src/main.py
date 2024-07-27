for i in range(6,0,-1):
  for j in range(i):
    print("*",end="")
  print("")
  
for i in range(6):
  for j in range(i):
    print("#",end="")
  print("")


for i in range(1,8):
  for j in range(i*2):
    print("*",end="")
  print("")
  

for i in range(10):
    for j in range(i):
        print("",end="")
    for k in range(2*i+1):
        print("@",end="")
    print("")
    
  

for i in range(10):
    for j in range(10-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("₹$",end="")
    print("")

for i in range(1,12,2):
    for j in range(i):
        print("₱",end="")
        print(" ",end="")
    print("*")
    
    
def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1 or j == 0 or j == n-1):
                print("=", end=" ")
            else:
                print(" ", end=" ")
        print()

n=int(input("Enter a Number of Rows:"))
print_pattern(n)

for i  in range(21,0,-2):
    for j in range(i):
        print("∆",end="")
    print("")
    
    
    
    
    