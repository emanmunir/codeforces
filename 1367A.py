t = int(input())
for _ in range(t):
    k = list(map(str,input()))
    for i in range(1,len(k)-1):
        if k[i] == k[i+1]:
            k[i+1] = ""
    print(''.join(k))