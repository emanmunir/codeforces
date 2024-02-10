t = int(input())
for i in range(t):
    ln = int(input())
    l = list(map(int,input().split()))
    for j in range(ln):
        if l.count(l[j]) == 1:
            print(j+1)
            break