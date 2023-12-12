
M1=[]
M2=[]
def matrix(M1):  
    global m
    global n
    m=int(input("Enter the number of rows in 1st Matrix"))
    n=int(input("Enter the number of columns in 1st Matrix"))
    print("Enter the Elements for 1st matrix")
    for i in range (m):
        A=[]
        for j in range (n):
            A.append(int(input()))
        M1.append(A)
    print("1st Matrix Entered Succeessfully\n",M1)
matrix(M1)

def matrix(M2):    
    m=int(input("Enter the number of rows in 2nd Matrix"))
    n=int(input("Enter the number of columns in 2nd Matrix"))
    print("Enter the Elements for 2nd matrix")
    for i in range (m):
        B=[]
        for j in range (n):
            B.append(int(input()))
        M2.append(B)
    print("2nd Matrix Entered Succeessfully\n",M2)
matrix(M2)

M3=[]
def add_matrices(M1,M2,M3):
    for i in range (len(M1)):
        C=[]
        for j in range (len(M2)):
            C.append(M1[i][j]+M2[i][j])
        M3.append(C)
    print("Addition Of Matrices is\n",M3)
add_matrices(M1,M2,M3)

M4=[]
def sub_matrices(M1,M2,M4):
    for i in range (len(M1)):
        D=[]
        for j in range (len(M2)):
            D.append(M1[i][j]-M2[i][j])
        M4.append(D)
    print("Subtraction Of Matrices is\n",M4)
sub_matrices(M1,M2,M4)

M5=[]
def mul_matrices(M1,M2,M5):
    for i in range (len(M1)):
        E=[]
        for j in range (len(M2)):
            sum=0
            for k in range (n):
                sum=sum+(M1[i][k]*M2[k][j])
            E.append(sum)
        M5.append(E)
    print("Multiplication of Matrices is\n",M5)
mul_matrices(M1,M2,M5)

M6=[]
def transpose(M1,M6):
    for i in range (n):
        F=[]
        for j in range (m):
            F.append(M1[j][i])
        M6.append(F)
    print("Transpose of 1st Matrix is\n",M6)
transpose(M1,M6)
