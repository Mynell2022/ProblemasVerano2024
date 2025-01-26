a,b,c = sorted(list(map(int,input().split())))
print(max(b-a-1,c-b-1))