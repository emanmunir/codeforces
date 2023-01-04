p = str(input())
for i in range(len(p)):
    if (ord(p[i])>= 33 and ord(p[i])<=126) and (len(p)>= 1 and len(p)<=100) and (len(p) != ""):
        if p[i] == "H" or p[i] == "Q" or p[i] == "9":
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        print("NO")
        break
