def count_even_betweenodd(arr):
    count=0
    for i in range(1,len(arr)-1):
        if arr[i]%2==0 and arr[i-1]%2==1 and arr[i+1]%2==1:
            count+=1
    return count
N=int(input())
arr=list(map(int,input().split()))
result=count_even_betweenodd(arr)
print(result)