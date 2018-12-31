
# coding: utf-8

# In[36]:

c=[]
N = int(input("Kare matrisin tipini giriniz: "))

A=[[[] for i in range (N)] for j in range (N)]
for i in range (N):
    for j in range (N):
        A[i] [j]=int(input("A(%d,%d)= "%(i+1,j+1)))

B=[[[] for i in range (N)] for j in range (N)]
for i in range (N):
    for j in range (N):
        B[i] [j]=int(input("B(%d,%d)= "%(i+1,j+1)))

for i in range(len(A)):
    for j in range(len(A[0])):
        c.append(A[i][j] + B[i][j])
print(c)

