
A=[]
def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   for i in range(n):
      x = float(input("Enter the  first year percentage of student %d : "%(i+1)))
      A.append(x)
   print("Array accepted successfully\n",A)
accept_array(A)

def partition(A,low,high) :
   i=low+1
   j=high
   while(j>=i) :
      while(j>=i and A[low] >= A[i]) :
         i = i + 1
      while(A[low] <A[j]) :
         j = j - 1
      if(j>i) :
         temp = A[j]
         A[j] = A[i]
         A[i] = temp
   temp = A[low]
   A[low] = A[j]
   A[j] = temp
   return j

def Quicksort(A,low,high) :
   if(low<high) :
      mid = partition(A,low,high)
      Quicksort(A,low,mid-1)
      Quicksort(A,mid+1,high)
      
def Main() :
   print("Marks before sorting")
   print(A)
   n =len(A)
   Quicksort(A,0,n-1)
   print("Marks after sorting")
   print(A)
   
   if(n >= 5) :
      print("Top Five Scores : ")
      for i in range(n-1,n-6,-1) :
         print(A[i])
   else :
      print("Top Scorers : ")
      for i in range(n-1,-1,-1) :
         print(A[i])                               
Main()