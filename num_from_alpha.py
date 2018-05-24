s=list(input(''))
a=[]
for x in s:
  if(x.isdigit()==True):
    a.append(x)
print(''.join(str(i) for i in a))
