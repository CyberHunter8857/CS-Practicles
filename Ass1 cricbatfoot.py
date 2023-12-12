Cricket=[]
Badminton=[]
Football=[]
A=int(input("no of students who paly cricket:"))
for n in range(0,A):
    a=str(input("enter name of student:"))
    Cricket.append(a)
print(Cricket)

B=int(input("no of students who paly badminton:"))
for n in range(0,B):
    b=str(input("enter name of student:"))
    Badminton.append(b)
print(Badminton)

C=int(input("no of students who paly football:"))
for n in range(0,C):
    c=str(input("enter name of student:"))
    Football.append(c)
print(Football)

def first(Cricket,Badminton):  
    newlist=[]
    len1=len(Cricket)
    len2=len(Badminton)
   
    for i in range(len1):
        for j in range(len2):
            if(Cricket[i]==Badminton[j]):
                newlist.append(Cricket[i])
                break
    print("list of students who play both cricket and badminton",newlist)
first(Cricket,Badminton)

def second(Cricket,Badminton):
    newlist=[]
    flag=0
    len1=len(Cricket)
    len2=len(Badminton)
    for i in range(len1):
        for j in range(len2):
            if(Cricket[i]==Badminton[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(Cricket[i])
        flag=0
    for i in range(len2):
        for j in range(len1):
            if(Badminton[i]==Cricket[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(Badminton[i])
        flag=0
    print("list of students who play either cricket or badminton",newlist)
second(Cricket,Badminton)

def third(Cricket,Football,Badminton):
    newlist=[]
    flag=0
    len1=len(Cricket)
    len2=len(Badminton)
    len3=len(Football)
    for i in range(len3):
        for j in range(len1):
            if(Football[i]==Cricket[j]):
                flag=1
                break
        for var in range(len2):
            if(Football[i]==Badminton[var]):
                flag=1
                break
        if(flag==0):
            newlist.append(Football[i])
        flag=0
    print("students who play neither cricket nor badminton",newlist)
third(Cricket,Football,Badminton)

def fourth(Cricket,Badminton,Football):
    list1=[]
    newlist=[]
    len1=len(Cricket)
    len2=len(Badminton)
    len3=len(Football)
    flag=0
    for i in range(len1):
        for j in range(len3):
            if(Cricket[i]==Football[j]):
                list1.append(Cricket[i])
                break
    lena=len(list1)
    for i in range(lena):
        for j in range(len2):
            if(list1[i]==Badminton[j]):
                flag=1
                break
        if(flag==0):
            newlist.append(list1[i])
        flag=0   
    print("students who play cricket football but not badminton",newlist)
fourth(Cricket,Badminton,Football)
