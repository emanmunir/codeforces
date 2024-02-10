for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    num = list(map(int,input()))
    for i in range(len(num)):   
        if b > num[i]:
            num.insert(i,b)
            break
        else:
            num.insert(i+1,b)
    new=([str(i) for i in num])
    print("".join(new))
