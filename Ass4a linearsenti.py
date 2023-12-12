A=[]
def accept_array(A):
    global n
    n=int(input("Enter the total number of students:"))
    for i in range (n):
        x=int(input("Enter the Roll No of Student :"))
        A.append(x)
    print("Students Info Accepted successfully\n",A)
    return n
accept_array(A)

def linear_search(A):
    print("LINEAR")
    global X
    X=int(input("Enter the Values to be search:"))
    for i in range (len(A)):
        if (A[i]==X):
            print("Student found at position",i)
            break
    else:
        print("Student not found")
linear_search(A)

def sentinel_search(A,n):
    print("SENTINAL")
    Y=int(input("Enter the values to be search:"))
    last= A[n-1]
    i=0
    while (A[i]!=Y):
        i=i+1
    A[n-1]= last
    if ((i< n-1) or (Y==A[n-1])):
        print("Student found",i)
    else:
        A.append(Y)
        print("New List",A)
        print("Student is at position",n)
sentinel_search(A,n)
