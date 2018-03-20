N=int(input("Enter limit:"))
a=[]
for i in range(0,N):
  b=int(input("Enter value:"))
  a.append(b)
print(a)
K=int(input("Value:"))
print( a[K-1] )
