N=int(input())
l=list(map(int,input().split(' ')))
for i in range(N):
    if(l[i]>l[i+1]):
        print(i+1)
        break
