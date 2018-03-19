A=int(input('1st value:'))
B=int(input('2nd value:'))
if(A>B):
    min1=A
else:
    min1=B
while(1):
    if(min1%A==0 and min1%B==0):
      print("LCM is :",min1)
      break
    min1=min1+1
  
