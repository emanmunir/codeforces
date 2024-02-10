a = input()
b = input()
for i in range(len(b)):
    if int(a[i])!= int(b[i]):
        print(1,end="")
    if int(a[i])== int(b[i]):
        print(0,end="")



