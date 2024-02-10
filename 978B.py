t = int(input())
c = 0
st = list(map(str,input()))
for i in range(t-2):
    if st[i]=="x" and st[i+1] == "x" and st[i+2]=="x":
        c +=1
print(c)
