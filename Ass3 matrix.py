A=[]

def accept_array(A):
    n=int(input("Enter the number of students: "))
    for i in range (n):
        x=float(input("Enter FE percentage of student: "))
        A.append(x)
    print("Data entered succesfully!\n",A)
accept_array(A)

def selection_sort(A):
    print("selection")
    n = len(A)
    for j in range(n-1):
        min=j
        for i in range (j+1,n):
            if(A[i] < A[min]):
                min=i
        temp=A[j]
        A[j]=A[min]
        A[min]=temp
    print("Here is your Sorted array\n",A)
selection_sort(A)

def bubble_sort(A):
    print("bubble")
    n = len(A)
    for k in range(1,n):
        for i in range(n-k):
            if(A[i] < A[i+1]):
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
    print("Here is your Sorted array\n",A)

    if(len(A)>=5):
        print("Top 5 scores: ")
        for i in range (5):
            print(A[i])
    else :
       print("Top Scorers : ")
       for i in range(len(A)) :
          print(A[i])                  
bubble_sort(A)
