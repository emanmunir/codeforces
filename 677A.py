people, h = map(int,input().split())
t = list(map(int,input().split()))
c = 0
for i in range(len(t)):
    if h < t[i]:
        c+= 2
    elif h >= t[i]:
        c+= 1
print(c)
