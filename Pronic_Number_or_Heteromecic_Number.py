def pronic(n):
    for i in range(int(n**0.5)+1):
        if i*(i+1)==n:
            return True
    return False
numb=int(input())
if pronic(numb):
    print("YES")
else:
    print("NO")