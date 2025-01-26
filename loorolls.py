l, n = map(int, input().split())
c=0
while(True):
    num=l
    num -= n*((l//n))
    c+=1
    if(n < 1 or num==0):
        break
    n -= num
print(c)