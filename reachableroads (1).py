n = int(input())
for _ in range(n):
    m = int(input())
    r = int(input())
    a = []
    for _ in range(m):
        a.append([])
    for _ in range(r):
        u,v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    b = [False]*m
    c= -1
    for i in range(m):
        if not b[i]:
            pila = [i]
            while pila:
                actual = pila.pop()
                if not b[actual]:
                    b[actual]= True
                    for j in a[actual]:
                        if not b[j]:
                            pila.append(j)
            c += 1
    print(c)