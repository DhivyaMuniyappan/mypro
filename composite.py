n=int(input(''))
for i in range(2,n):
  if(n%i==0):
    print("Yes")
    break
else:
  print('No')
