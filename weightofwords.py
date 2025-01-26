n, w = map(int, input().split())
if w< n or w > 26*n:
    print("impossible")
else:
    for i in range(n):
        m = min(w-(n-i-1),26)
        print(chr(ord('a') + m-1), end='')
        w -= m
    print()