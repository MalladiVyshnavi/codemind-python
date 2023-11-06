n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=list(s)
a.sort()
if len(a)>=1:
    print(a[-1])
else:
    print(-1)