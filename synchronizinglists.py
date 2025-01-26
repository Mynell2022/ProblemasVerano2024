while True:
    n =int(input())
    if n==0:
        break
    a, b= [], []
    for _ in range(n):
        a.append(int(input()))
    for _ in range(n):
        b.append(int(input()))

    orden ={num: i for i,num in enumerate(sorted(a))}
    b.sort()

    for num in a:
        print(b[orden[num]])
    print()