A=[]
def accept(A):
    global n
    n = int(input("Enter the total no. of student : "))
    print("Input roll numbers in sorted order")
    for i in range(n):
        x = int(input("Enter the  roll no of student %d : "%(i+1)))
        A.append(x)
    print("Student Info accepted successfully\n\n")
    return n
accept(A)

u=1
l=len(A)
X = int(input("Enter the roll_no to be searched for Binary Search: "))
def Re_Bsearch(A,u,l,X):
    if(u<=l ) :
       mid = int((u+l) / 2)
       if(A[mid] == X) :
          return mid      
       else :
          if(X < A[mid] ) :
             return Re_Bsearch(A,u,mid-1,X)
          else :
             return Re_Bsearch(A,mid+1,l,X)
    return -1 
tag = Re_Bsearch(A,0, n - 1, X)
if tag == -1:
    print("\tRoll no to be Searched not Found in Binary Search\n")
else:
    print("\tRoll no found at location %d in Binary Search" % (tag + 1))

Y = int(input("Enter the roll_no to be searched for Fibonacci Search: "))
def Fsearch(A,n,Y):
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    offset = -1
    while (f3 < n) :
       f1 = f2
       f2 = f3
       f3  = f1 + f2
    while (f3 > 1) :
       i = min(offset+f1, n-1)
       if(A[i] == Y) :
          return i        
       else :
          if (Y < A[i] ) :   
             f3  = f1
             f2 = f2 - f1
             f1 = f3 - f2
          else :     
             f3  = f2
             f2 = f1
             f1 = f3 - f2
             offset = i
    if(f2 == 1 and (offset+1) < n and A[offset + 1] == Y) :      
       return offset+1      
    return -1  
tag = Fsearch(A,n, Y)
if tag == -1:
    print("\tRoll no to be Searched not Found in Fibonacci Search\n")
else:
    print("\tRoll no found at location %d in Fibonacci Search" % (tag + 1))
print("End of program")