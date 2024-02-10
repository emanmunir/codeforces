t = int(input())
for _ in range(t):
    st = str(input())
    l = str(input())
    for i in range(0,len(st),2):
        if st[i]==l:
            print("YES")
            break
    else:
        print("NO")