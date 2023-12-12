A=[]
def accept(A):
    n=int(input("Enter total number of students"))
    for i in range (n):
        while True:
            x=input("Enter Marks of FDS")
            if(x=="AB"):
                x=-1
                break
            x=int(x)
            if(x>=0 and x<=30):
                break
            else:
                print("Enter valid marks")
        A.append(x)
    print("Marks stored Succesfully",A)
accept(A)

def avg(A):
    sum=0
    for i in range(len(A)):
        if(A[i]!=-1):
            sum=sum+A[i]
        aveg=sum/len(A)
    print("Average Marks is :",aveg)
avg(A)

def highlow(A):
    min=-1
    max=31
    for i in range(0,len(A)):
        if(min<A[i]):
            min=A[i]
        if(max>A[i] and A[i]!=-1):
            max=A[i]
    print("Highest Marks",min)
    print("Lowest marks",max)
highlow(A)

def absent(A):
    count=0
    for i in range (len(A)):
        if(A[i]==-1):
            count+=1
    print("Total Absent Students are :",count)
absent(A)

def frequ(A):
    freq=0
    for i in range (len(A)):
        count=0
        if(A[i]!=-1):
            for j in range(len(A)):
                if (A[i]==A[j]):
                    count+=1
        if(freq<count):
            freq=count
            mark=A[i]
    print("Marks with highest frequency is ",(mark,freq))
frequ(A)