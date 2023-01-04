n = int(input())
s =""
for i in range(1,n+1):
    if i%2 != 0:
        s+= f"I hate "
        if i == n:
            s+= f"it "
        else:
            s+= f"that "
    if i%2 == 0:
        s+= f"I love "
        if i == n:
            s+= f"it "
        else:
            s+= f"that "
print(s)
