str1 = str(input())
c0 = "0000000"
c1 = "1111111"
while len(str1) <= 100:
    if (c0 in str1) or (c1 in str1):
        print("YES")
    else:
        print("NO")
    break


