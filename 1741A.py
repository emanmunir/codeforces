for _ in range(int(input())):
    a,b = list(map(str,input().split()))
    xa,xb = 0,0
    for i in range(50):
        if a[i] == "X":
            xa += 1
        if b[i] == "X":
            xb += 1
        if ("S" in a) and ("M" or "L" in b):
            print("<")
        if ("S" in b) and ("M" or "L" in a):
            print(">")
        if ("")