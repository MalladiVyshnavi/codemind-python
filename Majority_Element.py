n=int(input())
lst=list(map(int,input().split()))
print(max(set(lst),key=lst.count))