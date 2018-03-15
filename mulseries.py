num=int(input("Enter your lucky num:"))
arr=[]
for d in range(1,6,1):
  arr.append(num*d)
print("  ".join(str(X) for X in arr))
