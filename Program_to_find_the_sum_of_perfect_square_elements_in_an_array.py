import math
def sum_perfect_square(arr):
    square_sum=0
    for num in arr:
        if math.isqrt(num)**2==num:
            square_sum=square_sum+num
    return square_sum
array_size=int(input())
array=list(map(int,input().split()))
result=sum_perfect_square(array)
print(result)