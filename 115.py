N=int(input("Enter limit:"))
n=[]
for i in range(0,N):
  b=int(input("Ur num:"))
  n.append(b)
print(n)
n.sort()
print(n)
K=int(input("Enter num:"))
print(n[K-1])
