s1,s2=input().split(' ')
c=0
for i in range(len(s1)):
  if(s1[i]!=s2[i]):
    c=c+1
if(c==1):
  print("Yes")
else:
  print("No")
