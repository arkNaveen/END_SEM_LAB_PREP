# NAVEEN K
# EC21B1030
import numpy as np

m1 = int(input("Enter no. of rows of Matrix A "))
n1 = int(input("Enter no. of columns of Matrix A "))
m2 = int(input("Enter no. of rows of Matrix B "))
n2 = int(input("Enter no. of columns of Matrix B "))

if m1 != m2 and n1 != n2:
    print("Row Column Mismatch Error")
    exit(1)
shape1 = (m1,n1)
a = np.zeros(shape1)
for i in range(m1):
    for j in range(n1):
        a[i,j] = int(input("Enter "+str(i)+"th and"+str(j)+"th element"))
print(a)


shape2 = (m2,n2)
b = np.zeros(shape2)
for i in range(m2):
    for j in range(n2):
        b[i,j] = int(input("Enter "+str(i)+"th and"+str(j)+"th element"))
print(b)

# Addition
ad = np.add(a,b)
print("Addition Of Matrices")
print(ad)

# Substraction
su = np.subtract(a,b)
print("Substraction Of Matrices")
print(su)

# Multiplication
if n1 == m2:
    mu = np.matmul(a,b)
    print("Multiplication Of Matrices")
    print(mu)
else:
    print("Multiplication not Possible")
# Scalar Multiplication
sc = int(input("Enter scalar for multiplication with A "))
sm = a * sc
print("Scalar Multiplication ")
print(sm)

# Elementwise Multiplication
em = np.multiply(a,b)
print("Elementwise Multiplication ")
print(em)
