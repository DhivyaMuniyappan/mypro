line=int(input(''))
arr=[]
for i in range(line):
   kabali,opponent=map(int,input().split(' '))
   arr.append(abs(kabali-opponent))
for i in arr:
  print(i)
