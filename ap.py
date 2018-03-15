num=int(input("Enter your lucky num:"))
first=int(input("Enter your first num:"))
diff=int(input("Enter your diff num:"))
sum=0
num=num+1
for i in range(first,num):
  sum=sum+i
  i=sum+diff
  print(sum)
  
