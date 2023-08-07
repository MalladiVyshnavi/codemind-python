n=int(input())
b=list(map(int,input().split()))
s=""
for i in b:
    i=str(i)
    s=s+i
s=int(s)+1
s=str(s)
for i in s:
    print(i,end=" ")